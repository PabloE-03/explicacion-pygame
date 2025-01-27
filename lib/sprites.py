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

def imp():
    imp = sprite.Sprite()
    
    imp.spriteSheet = image.load("./img/imp-spritesheet.png").convert()

    frames.imp_abajo(imp)
    frames.imp_ataque(imp)

    imp.rect.x = 75
    imp.rect.y = 300

    return imp

def fireball():
    fireball = sprite.Sprite()

    fireball.spriteSheet = image.load("./img/fireball.png").convert()

    frames.fireball_frames(fireball)

    # no deben de aparecer hasta que el imp ataque
    fireball.rect.x = 800
    fireball.rect.y = 600

    return fireball

def bala():
    bala = sprite.Sprite()

    bala.image = image.load("./img/bala.png")

    bala.rect = bala.image.get_rect()

    bala.rect.x = 850
    bala.rect.y = 650

    return bala