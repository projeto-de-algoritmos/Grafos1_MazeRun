import pygame
import button

SCREEN_HEIGHT = 500
SCREEN_WIDHT = 800

screen = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HEIGHT))
pygame.display.set_caption('Maze Run')

start_img = pygame.image.load('images/start_btn').convert_alpha()
exit_img = pygame.image.load('images/exit_btn').convert_alpha()

start_button = button.Button(100, 200, start_img, 0.8)
exit_button = button.Button(450, 200, exit_img, 0.8)

run = True
while run:

    screen.fill((79, 179, 159))

    if start_button.draw(screen):
        print('START')
    if exit_button.draw(screen):
        pygame.event.post(pygame.event.Event(pygame.QUIT))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
