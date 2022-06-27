from mainScreen import *
from mazegenerator import *
import mainScreen


def iniciar():
    game = startgame()
    if game == True:
        nivel = menu_principal()
        if nivel == 1:
            desenhar(1)
        else:
            desenhar(2)    

def callmenu():
    dificuldade = mainScreen.menu_principal()
    if dificuldade == 1:
        desenhar(1)
    else:
        desenhar(2)


if __name__ == '__main__':
    iniciar()
    