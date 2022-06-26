from mainScreen import *
from mazegenerator import *

def iniciar():
    game = startgame()
    if game == True:
        desenhar()

def reiniciar():
    desenhar()

if __name__ == '__main__':
    iniciar()