import pygame
import lib.sprites as sprites
import lib.eventos as eventos
import lib.frames as frames
import lib.colisiones as colisiones
import random

def admin(superficie,doomguy,texto):
    teclas_admin = pygame.key.get_pressed()
    if(teclas_admin[pygame.K_u]):
        superficie=True
    if(teclas_admin[pygame.K_z]):
        doomguy = sprites.doomguy()
        superficie = False
        texto = False
    if(teclas_admin[pygame.K_p]):
        texto = True
    return superficie,doomguy,texto
# variables de administracion
superficie = False
texto = False
# definicion de la escena
WIDTH = 800
HEIGHT = 600 

# variables del juego
running = True
derecha = 0
izquierda = 0
arriba = 0
abajo = 0
disparo = False
despliegue_bala = False
derecha_bala = 0
izquierda_bala = 0
t_disparo = 0
derecha_imp = 0
izquierda_imp = 1
ataque_imp = False
vel_imp = 3
tiempo_ataque_imp = [random.randint(100,300),0,0] # primer valor, valor tiempo de espera de ataque, segundo valor contador de cooldown, tercer valor animacion
fase = 1
animacion_fireball = 0
derecha_f = 0
izquierda_f = 0
despliegue = False
# instancia de pygame
pygame.init()

# escenario
screen = pygame.display.set_mode(size=(WIDTH,HEIGHT))

# fps
fps = pygame.time.Clock()
# sprites
tot_sprites = [
    sprites.terreno(),
    sprites.doomguy(),
    sprites.imp(),
    sprites.fireball(),
    sprites.fireball(),
    sprites.bala(),
    sprites.bala()
]


# bucle donde se define el juego
while running:

    # finalizamos el juego si pulsamos la X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # movimiento del personaje
    if(not disparo):
        derecha,izquierda,arriba,abajo = eventos.movimiento(tot_sprites[1],derecha,izquierda,abajo,arriba)
        colisiones.doomguy_collide(tot_sprites[1])
        disparo = eventos.evento_disparo()
    # animacion de andar
    frames.actualizar_frames_personaje(tot_sprites[1],arriba,derecha,izquierda,abajo,disparo)
    # animacion de disparo
    if(disparo):
        t_disparo,disparo,despliegue_bala = frames.animacion_disparo(tot_sprites[1],t_disparo,disparo,derecha,izquierda,despliegue_bala)
        if(despliegue_bala):
            derecha_bala,izquierda_bala = eventos.despliegue_proyectil([tot_sprites[5],tot_sprites[6]],tot_sprites[1],derecha_bala,izquierda_bala,derecha,izquierda)
            despliegue_bala = False

    # movimiento del imp
    if(not ataque_imp):
        eventos.movimiento_imp(tot_sprites[2],derecha_imp,vel_imp)
        # animacion de andar
        frames.actualizar_frames_imp(tot_sprites[2])

        tiempo_ataque_imp[0],tiempo_ataque_imp[1],ataque_imp = eventos.ataque_imp(tiempo_ataque_imp[0],tiempo_ataque_imp[1],ataque_imp,fase)
    else:
        tiempo_ataque_imp[2],ataque_imp,despliegue = frames.animacion_ataque(tot_sprites[2],tiempo_ataque_imp[2],derecha_imp,ataque_imp,despliegue)
        # ataque del imp
        if(despliegue):
            derecha_f,izquierda_f =  eventos.despliegue_proyectil([tot_sprites[3],tot_sprites[4]],tot_sprites[2],derecha_f,izquierda_f,derecha_imp,izquierda_imp)

    # movimiento de la bala
    eventos.movimiento_proyectil([tot_sprites[5],tot_sprites[6]],derecha_bala,12)

    # colision de la bala
    derecha_bala,izquierda_bala = colisiones.proyectil_collide([tot_sprites[4],tot_sprites[5]],derecha_bala,izquierda_bala)
    # movimiento del ataque del imp
    eventos.movimiento_proyectil([tot_sprites[3],tot_sprites[4]],derecha_f,9)

    # animacion del ataque del imp
    animacion_fireball = frames.animacion_fireball(tot_sprites[3],derecha_f,animacion_fireball)
    animacion_fireball = frames.animacion_fireball(tot_sprites[4],derecha_f,animacion_fireball)

    # colision del imp
    derecha_imp,izquierda_imp = colisiones.imp_collide(tot_sprites[2],derecha_imp,izquierda_imp)
    # colision fireball
    derecha_f,izquierda_f = colisiones.proyectil_collide([tot_sprites[3],tot_sprites[4]],derecha_f,izquierda_f)
    # acierto de la bala con el imp
    fase = colisiones.bala_collide(tot_sprites[5],tot_sprites[2],fase)
    fase = colisiones.bala_collide(tot_sprites[6],tot_sprites[2],fase)
    # pintar multiples sprites
    for sprite in tot_sprites:
        screen.blit(source=sprite.image,dest=(sprite.rect.x,sprite.rect.y))
    
    if(fase==1):
        vel_imp=3
    elif(fase==2):
        vel_imp=4.5
    else:
        vel_imp=6
    
    if (superficie):
        tot_sprites[1].image.fill((255,0,0))
    if(texto):
        fuente = pygame.font.Font(None,35)
        textoX = "coords x:"+str(tot_sprites[1].rect.x)
        transmitirX = fuente.render(textoX,1,(255,255,255))
        screen.blit(transmitirX,(100,500))
        textoY = "coords y:"+str(tot_sprites[1].rect.y)
        transmitirY = fuente.render(textoY,1,(255,255,255))
        screen.blit(transmitirY,(100,540))

    superficie,tot_sprites[1],texto = admin(superficie,tot_sprites[1],texto)

    # repintado de la pantalla
    pygame.display.flip()
    fps.tick(60)

# fin del juego
pygame.quit()