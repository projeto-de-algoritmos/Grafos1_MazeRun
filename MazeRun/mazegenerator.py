import pygame

RES = WIDTH, HEIGHT = 1200, 900
TILE = 100
cols, rows = WIDTH // TILE, HEIGHT // TILE

pygame.init()
source = pygame.display.set_mode(RES)
clock = pygame.time.Clock()


class Cell:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
        self.visited = False

    def draw_current_cell(self):
        x, y = self.x * TILE, self.y * TILE
        pygame.draw.rect(source,pygame.Color('black'),(x+2,y+2,TILE-2,TILE-2))  

    def draw(self):
        x, y = self.x * TILE, self.y * TILE
        if self.visited:
            pygame.draw.rect(source,pygame.Color('black'),(x,y,TILE,TILE))

        if self.walls['top']:
            pygame.draw.line(source, pygame.Color('grey'), (x, y), (x + TILE, y), 2)
        if self.walls['right']:
            pygame.draw.line(source, pygame.Color('grey'), (x + TILE, y), (x + TILE, y + TILE), 2)
        if self.walls['bottom']:
            pygame.draw.line(source, pygame.Color('grey'), (x + TILE, y + TILE), (x , y + TILE), 2)
        if self.walls['left']:
            pygame.draw.line(source, pygame.Color('grey'), (x, y + TILE), (x, y), 2)


grid_cells=[Cell(col,row)for row in range(rows)for col in range(cols)]
current_cell=grid_cells[0]


while True:
    source.fill(pygame.Color('darkslategray'))
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    [cell.draw() for cell in grid_cells]
    current_cell.visited=True
    current_cell.draw_current_cell()
    
    pygame.display.flip()
    clock.tick(30)