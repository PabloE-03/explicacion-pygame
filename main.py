import pygame
import lib.sprites as sprites
import lib.eventos as eventos
import lib.frames as frames
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
t_disparo = 0
# instancia de pygame
pygame.init()

# escenario
screen = pygame.display.set_mode(size=(WIDTH,HEIGHT))

# fps
fps = pygame.time.Clock()
# sprites
tot_sprites = [
    sprites.terreno(),
    sprites.doomguy()
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
        disparo = eventos.evento_disparo()
    # animacion de andar
    frames.actualizar_frames_personaje(tot_sprites[1],arriba,derecha,izquierda,abajo,disparo)
    # animacion de disparo
    if(disparo):
        t_disparo,disparo = frames.animacion_disparo(tot_sprites[1],t_disparo,disparo,derecha,izquierda)
    # pintar multiples sprites
    for sprite in tot_sprites:
        screen.blit(source=sprite.image,dest=(sprite.rect.x,sprite.rect.y))

    # repintado de la pantalla
    pygame.display.flip()
    fps.tick(60)

# fin del juego
pygame.quit()