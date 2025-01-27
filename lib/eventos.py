import pygame
import random
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

def movimiento_imp(imp,derecha_imp,vel):
    if(derecha_imp==0):
        imp.rect.y -= vel
    else:
        imp.rect.y += vel

def ataque_imp(cooldown,tiempo,ataque,fase):
    if(tiempo<cooldown):
        tiempo+=1
    else:
        ataque = True
        if(fase==0):
            cooldown = random.randint(100,300)
        if(fase==1):
            cooldown = random.randint(80,250)
        else:
            cooldown = random.randint(60,200)
        tiempo = 0
    return cooldown,tiempo,ataque

def despliegue_proyectil(fireballs,imp,derecha,izquierda,derecha_imp,izquierda_imp):
    derecha = derecha_imp
    izquierda = izquierda_imp
    if(fireballs[1].rect.x!=800 and fireballs[1].rect.y!=600):
        if(derecha==1):
            fireballs[0].rect.x = imp.rect.x + 30
        else:
            fireballs[0].rect.x = imp.rect.x
        fireballs[0].rect.y = imp.rect.y + 10

    if(fireballs[0].rect.x!=800 and fireballs[0].rect.y!=600):
        if(derecha==1):
            fireballs[1].rect.x = imp.rect.x + 30
        else:
            fireballs[1].rect.x = imp.rect.x
        fireballs[1].rect.y = imp.rect.y + 10
    else:
        if(derecha==1):
            fireballs[0].rect.x = imp.rect.x + 30 
        else:
            fireballs[0].rect.x = imp.rect.x 
        fireballs[0].rect.y = imp.rect.y + 10

    return derecha,izquierda


def movimiento_proyectil(fireballs,derecha,vel):
    if(fireballs[1].rect.x>=800 and fireballs[1].rect.y>=600):
        if(derecha):
            fireballs[0].rect.x+=vel
        else:
            fireballs[0].rect.x-=vel
    elif(fireballs[0].rect.x>=800 and fireballs[0].rect.y>=600):
        if(derecha):
            fireballs[1].rect.x+=vel
        else:
            fireballs[1].rect.x-=vel
    else:
        if(derecha):
            fireballs[0].rect.x+=vel
            fireballs[1].rect.x+=vel
        else:
            fireballs[0].rect.x-=vel
            fireballs[1].rect.x-=vel