import pygame
import button
import sys
from button import *
import controlergamer

'''
Tela inicial do jogo, instancia o botão start e quit
'''


pygame.init()

RES1 = WIDTH, HEIGHT = 1200, 900


screen = pygame.display.set_mode((RES1))
pygame.display.set_caption('Maze Run')

# fonte dos textos da tela
def get_font(size): 
    return pygame.font.Font('assets/font.ttf', size)

def menu_principal():
    while True:
        screen.fill("black")

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("Maze  CROAC", True, "Blue")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = ButtonScreentwo(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="EASY", font=get_font(75), base_color="White", hovering_color="Blue")
        OPTIONS_BUTTON = ButtonScreentwo(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="DIFICIL", font=get_font(75), base_color="White", hovering_color="Blue")
        QUIT_BUTTON = ButtonScreentwo(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="SAIR", font=get_font(75), base_color="White", hovering_color="Blue")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    return 1
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    return 2
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

# tela de inicio do jogo
def startgame():
    while True:
        screen.fill("black")

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("Maze  CROAC", True, "Blue")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = ButtonScreentwo(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="START", font=get_font(75), base_color="White", hovering_color="Blue")
        QUIT_BUTTON = ButtonScreentwo(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 400), 
                            text_input="SAIR", font=get_font(75), base_color="White", hovering_color="Blue")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    return True
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

# tela de derrota
def gameover():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("black")

        PLAY_TEXT = get_font(45).render("Você perdeu.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        screen.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = ButtonScreentwo(image=None, pos=(640, 460), 
                            text_input="JOGAR NOVAMENTE", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    print('entrou')
                    controlergamer.callmenu()
                    
                    

        pygame.display.update()

# tela de vitoria do jogo
def screenWinner():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("white")

        OPTIONS_TEXT = get_font(45).render("Parabéns você venceu AEEE.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = ButtonScreentwo(image=None, pos=(640, 460), 
                            text_input="JOGAR NOVAMENTE", font=get_font(75), base_color="Black", hovering_color="Green")
                            

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    controlergamer.callmenu()     

        pygame.display.update()