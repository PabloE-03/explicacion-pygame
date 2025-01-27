import pygame

def movimiento(sprite:pygame.sprite.Sprite,derecha,izquierda,abajo,arriba):
    """Metodo que gestiona la direccion del personaje principal

    Args:
        sprite (pygame.sprite.Sprite): sprite del personaje principal

    Returns:
        derecha,izquierda,arriba,abajo: deteccion de movimientos para la animacion
    """
    # deteccion de eventos de teclas
    teclas = pygame.key.get_pressed()

    # actualizacion de direccion

    if(teclas[pygame.K_d]):
        sprite.rect.x+=3
        derecha = 1
        izquierda = 0
        abajo = 0
        arriba = 0
    if(teclas[pygame.K_a]):
        sprite.rect.x-=3
        derecha = 0
        izquierda = 1
        abajo = 0
        arriba = 0
    if(teclas[pygame.K_w]):
        sprite.rect.y-=3
        derecha = 0
        izquierda = 0
        abajo = 0
        arriba = 1
    if(teclas[pygame.K_s]):
        sprite.rect.y+=3
        derecha = 0
        izquierda = 0
        abajo = 1
        arriba = 0
    else:
        sprite.rect.x += 0
        sprite.rect.y += 0

    return derecha,izquierda,arriba,abajo

def evento_disparo():
    teclas = pygame.key.get_pressed()
    
    if((teclas[pygame.K_SPACE] or teclas[pygame.K_e])):
        return True
    else:
        return False


    