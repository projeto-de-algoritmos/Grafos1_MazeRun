import pygame
import button
import sys
from button import *

 
pygame.init()

RES1 = WIDTH, HEIGHT = 1200, 900


screen = pygame.display.set_mode((RES1))
pygame.display.set_caption('Maze Run')

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font('assets/font.ttf', size)

def startgame():

    start_img = pygame.image.load('images/start_btn').convert_alpha()
    exit_img = pygame.image.load('images/exit_btn').convert_alpha()

    start_button = button.Button(100, 200, start_img, 0.8)
    exit_button = button.Button(450, 200, exit_img, 0.8)

    run = True
    while run:

        screen.fill((79, 179, 159))

        if start_button.draw(screen):
            return True
        if exit_button.draw(screen):
            pygame.event.post(pygame.event.Event(pygame.QUIT))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
 
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
                    pass
                    
                    

        pygame.display.update()

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
                    pass

        pygame.display.update()