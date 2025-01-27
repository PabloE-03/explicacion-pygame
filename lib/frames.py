import pygame
class Frames:
    def obtenerFrame(spriteSheet,x,y,width,height):
        BASE = pygame.Color(0,0,0)

        # obtencion del frame a convertir
        frame = pygame.Surface([width,height]).convert()

        # pintado del frame seleccionado - seleccionamos la hoja de sprites, su posicion inicial
        # y su valor de recta en posicion,ancho y largo
        frame.blit(spriteSheet,(0,0),(x,y,width,height))

        frame.set_colorkey(BASE)

        return frame

def doomguy_derecha_izquierda(doomguy):
    doomguy.frames_derecha = []

    # primer frame
    frame = Frames.obtenerFrame(doomguy.spriteSheet,0,0,85,114)

    doomguy.frames_derecha.append(frame)

    # segundo frame
    frame = Frames.obtenerFrame(doomguy.spriteSheet,87,0,74,114)

    doomguy.frames_derecha.append(frame)

    # tercer frame
    frame = Frames.obtenerFrame(doomguy.spriteSheet,163,0,73,114)

    doomguy.frames_derecha.append(frame)

    # cuarto frame
    frame = Frames.obtenerFrame(doomguy.spriteSheet,236,0,74,114)

    doomguy.frames_derecha.append(frame)

    doomguy.image = doomguy.frames_derecha[0]
    doomguy.rect = doomguy.image.get_rect()

    # generacion de frames para el lado izquierdo invirtiendo la imagen
    doomguy.frames_izquierda = [
        pygame.transform.flip(frame, True, False) for frame in doomguy.frames_derecha
    ]

def doomguy_abajo(doomguy):
    doomguy.frames_abajo = []

    # primer frame
    frame = Frames.obtenerFrame(doomguy.spriteSheet,0,115,82,114)

    doomguy.frames_abajo.append(frame)

    # segundo frame
    frame = Frames.obtenerFrame(doomguy.spriteSheet,83,116,74,114)

    doomguy.frames_abajo.append(frame)

    # tercer frame
    frame = Frames.obtenerFrame(doomguy.spriteSheet,157,116,77,114)

    doomguy.frames_abajo.append(frame)

    # tercer frame
    frame = Frames.obtenerFrame(doomguy.spriteSheet,234,115,81,114)

    doomguy.frames_abajo.append(frame)

def doomguy_arriba(doomguy):
    doomguy.frames_arriba = []

    # primer frame
    frame = Frames.obtenerFrame(doomguy.spriteSheet,0,229,71,108)

    doomguy.frames_arriba.append(frame)

    # segundo frame
    frame = Frames.obtenerFrame(doomguy.spriteSheet,73,229,69,108)

    doomguy.frames_arriba.append(frame)

    # tercer frame
    frame = Frames.obtenerFrame(doomguy.spriteSheet,144,229,74,108)

    doomguy.frames_arriba.append(frame)

    # cuarto frame
    frame = Frames.obtenerFrame(doomguy.spriteSheet,219,229,67,108)

    doomguy.frames_arriba.append(frame)

def doomguy_disparo(doomguy):
    doomguy.disparo_d = []

    # primer frame
    frame = Frames.obtenerFrame(doomguy.spriteSheet,0,442,107,108)

    doomguy.disparo_d.append(frame)
    # segundo frame
    frame = Frames.obtenerFrame(doomguy.spriteSheet,107,442,107,108)

    doomguy.disparo_d.append(frame)

    # generacion de frames para el lado izquierdo invirtiendo la imagen
    doomguy.disparo_i = [
        pygame.transform.flip(frame, True, False) for frame in doomguy.disparo_d
    ]

def actualizar_frames_personaje(spriteSheet,arriba,derecha,izquierda,abajo,disparo):
    # animacion de frames para el movimiento de derecha
    if(derecha == 1 and not disparo):
        frame  = (spriteSheet.rect.x // 40) % len(spriteSheet.frames_derecha)
        spriteSheet.image = spriteSheet.frames_derecha[frame]
    
    if(izquierda == 1 and not disparo):
        frame  = (spriteSheet.rect.x // 40) % len(spriteSheet.frames_izquierda)
        spriteSheet.image = spriteSheet.frames_izquierda[frame]

    if(abajo == 1 and not disparo):
        frame  = (spriteSheet.rect.y // 40) % len(spriteSheet.frames_abajo)
        spriteSheet.image = spriteSheet.frames_abajo[frame]

    if(arriba == 1 and not disparo):
        frame  = (spriteSheet.rect.y // 40) % len(spriteSheet.frames_arriba)
        spriteSheet.image = spriteSheet.frames_arriba[frame]


def animacion_disparo(spriteSheet,tiempo,disparo,derecha,izquierda):
    tiempo+=1
    if(izquierda == 1):
        if(tiempo<=5):
            spriteSheet.image = spriteSheet.disparo_i[0]
        elif(tiempo>5 and tiempo<=30):
            spriteSheet.image = spriteSheet.disparo_i[1]
        else:
            disparo = False
            tiempo = 0
            spriteSheet.image = spriteSheet.disparo_i[0]
    else:
        if(tiempo<=5):
            spriteSheet.image = spriteSheet.disparo_d[0]
        elif(tiempo>5 and tiempo<=30):
            spriteSheet.image = spriteSheet.disparo_d[1]
        else:
            disparo = False
            tiempo = 0
            spriteSheet.image = spriteSheet.disparo_d[0]
    return tiempo,disparo
