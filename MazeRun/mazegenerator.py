import pygame
from random import choice
import mainScreen

def desenhar():
    
    RES = WIDTH, HEIGHT = 1200, 900
    TILE = 100
    cols, rows = WIDTH // TILE, HEIGHT // TILE

    pygame.init()
    source = pygame.display.set_mode(RES)

    # Estrutura do Grafo DFS
    class Cell:
        def __init__(self, x, y):
            self.x, self.y = x, y
            self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
            self.visited = False
            self.thickness = 4

        def draw(self):
            x, y = self.x * TILE, self.y * TILE
            if self.visited:
                pygame.draw.rect(source,pygame.Color('black'),(x,y,TILE,TILE))
            if self.walls['top']:
                pygame.draw.line(source, pygame.Color('blue'), (x, y), (x + TILE, y), self.thickness)
            if self.walls['right']:
                pygame.draw.line(source, pygame.Color('blue'), (x + TILE, y), (x + TILE, y + TILE), self.thickness)
            if self.walls['bottom']:
                pygame.draw.line(source, pygame.Color('blue'), (x + TILE, y + TILE), (x , y + TILE), self.thickness)
            if self.walls['left']:
                pygame.draw.line(source, pygame.Color('blue'), (x, y + TILE), (x, y), self.thickness)

        def check_cell(self,x,y):
            find_index = lambda x,y : x + y * cols
            if x < 0 or x > cols- 1 or y < 0 or y > rows -1:
                return False
            return self.grid_cells[find_index(x,y)]

        def check_neighbors(self, grid_cells):
            self.grid_cells = grid_cells
            neighbors=[]
            top=self.check_cell(self.x,self.y-1)
            right=self.check_cell(self.x+1,self.y)
            bottom=self.check_cell(self.x,self.y+1)
            left=self.check_cell(self.x-1,self.y)
            if top and not top.visited:
                neighbors.append(top)
            if right and not right.visited:
                neighbors.append(right)
            if bottom and not bottom.visited:
                neighbors.append(bottom)
            if left and not left.visited:
                neighbors.append(left)
            return choice(neighbors) if neighbors else False
        
        def get_rects(self):
            rects = []
            x, y = self.x * TILE, self.y * TILE
            if self.walls['top']:
                rects.append(pygame.Rect( (x, y), (TILE, self.thickness) ))
            if self.walls['right']:
                rects.append(pygame.Rect( (x + TILE, y), (self.thickness, TILE) ))
            if self.walls['bottom']:
                rects.append(pygame.Rect( (x, y + TILE), (TILE , self.thickness) ))
            if self.walls['left']:
                rects.append(pygame.Rect( (x, y), (self.thickness, TILE) ))
            return rects


    def remove_parede(current, next):
        dx = current.x - next.x
        if dx == 1:
            current.walls['left'] = False
            next.walls['right'] = False
        elif dx == -1:
            current.walls['right'] = False
            next.walls['left'] = False
        dy = current.y - next.y    
        if dy == 1:
            current.walls['top'] = False
            next.walls['bottom'] = False
        elif dy == -1:
            current.walls['bottom'] = False
            next.walls['top'] = False

    def is_collide(x, y):
        tmp_rect = player_rect.move(x, y)
        if tmp_rect.collidelist(walls_collide_list) == -1:
            return False
        return True

    
    grid_cells=[Cell(col,row)for row in range(rows)for col in range(cols)]
    current_cell=grid_cells[0]
    stack=[] #pilha do dfs


    # Carregando Imagens dos jogadores
    sapo_img = pygame.image.load('images/sapo.png').convert_alpha()
    sapo1_img = pygame.image.load('images/sapo_1.png').convert_alpha()
    happy_img = pygame.image.load('images/happy.png').convert_alpha()
    speedPlayer = 2

    # settings do jogador
    player_img = pygame.transform.scale(sapo_img, (TILE - 15 * grid_cells[0].thickness, TILE - 15 * grid_cells[0].thickness))
    perereca_img = pygame.transform.scale(sapo1_img, (TILE - 10 * grid_cells[0].thickness, TILE - 10 * grid_cells[0].thickness))
    happy_img = pygame.transform.scale(happy_img, (TILE - 10 * grid_cells[0].thickness, TILE - 10 * grid_cells[0].thickness))

    player_rect = player_img.get_rect()
    player_rect.center = TILE // 2, TILE // 2

    perereca_rect = perereca_img.get_rect()
    perereca_rect.center = WIDTH-TILE//2, HEIGHT-TILE//2

    happy_rect = perereca_img.get_rect()
    happy_rect.center = WIDTH-TILE//2, HEIGHT-TILE//2

    sapo_sfx = pygame.mixer.Sound('sfx/parabens.mp3')
    sapo_sfx.set_volume(0.3)

    walls_collide_list = sum([cell.get_rects() for cell in grid_cells], [])
    walls_collide_list = []

    directions = {'a': (-speedPlayer, 0), 'd': (speedPlayer, 0), 'w': (0, -speedPlayer), 's': (0, speedPlayer)}
    keys = {'a': pygame.K_a, 'd': pygame.K_d, 'w': pygame.K_w, 's': pygame.K_s}
    direction = (0, 0)
    flag_sfx = 1


    #loop principal do jogo
    while True:
        source.fill(pygame.Color('darkslategray'))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        # controla movimentos do jogador
        pressed_key = pygame.key.get_pressed()
        for key, key_value in keys.items():
            if pressed_key[key_value] and not is_collide(*directions[key]):
                direction = directions[key]
                # print('aqui')
                break
            if  is_collide(*directions[key]):
                # print('bateu')
                mainScreen.gameover()
            else:
                pass
                # print('pqp')    
        if not is_collide(*direction):
            player_rect.move_ip(direction)

        # adiciona musica do jogo caso o usuario ganhe
        if player_rect.colliderect(perereca_rect) and flag_sfx == 1:
            sapo_sfx.play()
            flag_sfx = 0

        # desenha labirinto
        [cell.draw() for cell in grid_cells]


        # empilhando todas as celulas visitadas, escreve todas as células visitadas e se não houver para onde ir, pega o valor das etapas anteriores da pilha
        next_cell = current_cell.check_neighbors(grid_cells)
        if next_cell:
            next_cell.visited = True
            stack.append(current_cell)
            remove_parede(current_cell, next_cell)
            current_cell = next_cell
        elif stack:
            current_cell = stack.pop()

        walls_collide_list = sum([cell.get_rects() for cell in grid_cells], [])

        source.blit(player_img, player_rect)

        if flag_sfx == 1:
            source.blit(perereca_img, perereca_rect)
            print('entrou')
        else:
            source.blit(happy_img, happy_rect)
            mainScreen.screenWinner()
        pygame.display.flip()
