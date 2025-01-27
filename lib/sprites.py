import pygame.sprite as sprite
import pygame.image as image
import pygame
import lib.frames as frames
def terreno():
    terreno = sprite.Sprite()
    # cargado de la imagen - RUTAS DESDE LA RAIZ
    terreno.image = image.load("./img/terreno.png")

    # creacion de posiciones
    terreno.rect = terreno.image.get_rect()

    # posicion x
    terreno.rect.x = 0
    terreno.rect.y = 0

    # devolvemos el sprite con su posicion y superficie
    return terreno

def doomguy():
    doomguy = sprite.Sprite()
    
    doomguy.spriteSheet = image.load("./img/doomguy-spritesheet.png").convert()

    frames.doomguy_derecha_izquierda(doomguy)
    frames.doomguy_abajo(doomguy)
    frames.doomguy_arriba(doomguy)
    frames.doomguy_disparo(doomguy)

    doomguy.rect.x = 400
    doomguy.rect.y = 300

    return doomguy
