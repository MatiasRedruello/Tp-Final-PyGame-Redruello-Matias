import pygame
import sys
from clase_proyectil import Proyectil
from clase_jugador import Jugador
pygame.init()

# Configuración de la ventana
screen_width = 800 #set
screen_height = 600 #set
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Salto de un Rectángulo')

back_img = pygame.image.load("background/goku_house.png")# Cargo imagen de fondo. set
back_img = pygame.transform.scale(back_img, (screen_width, screen_height))#Adapto imagen a la pantalla 

# Lista para almacenar los proyectiles
bullets = pygame.sprite.Group()

#clock
clock = pygame.time.Clock()
fps = 60
clase_jugador = Jugador()
# Bucle principal del juego


shooting = False 
running_game = True

while running_game:
    letras_precionadas = pygame.key.get_pressed()
    lista_de_eventos = pygame.event.get()
    for event in lista_de_eventos:
        if event.type == pygame.QUIT:
            running_game = False

        # Detecta si se preciono la tecla de disparo a la derecha
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d :
            nuevo_proyectil = Proyectil(clase_jugador.rect.x, clase_jugador.rect.y,
                                        clase_jugador.rect.width,clase_jugador.rect.height,True)
            bullets.add(nuevo_proyectil)
        # Detecta si se preciono la tecla de disparo a la izquierda  
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            nuevo_proyectil = Proyectil(clase_jugador.rect.x,clase_jugador.rect.y,
                                        clase_jugador.rect.width,clase_jugador.rect.height,False)
            bullets.add(nuevo_proyectil)            
        

    # Dibujar el fondo
    screen.blit(back_img, back_img.get_rect())  # Color blanco como fondo

    # Dibujar el rectángulo en su nueva posición
    pygame.draw.rect(screen, (255,0,0),(clase_jugador.rect.x, clase_jugador.rect.y, clase_jugador.rect.width, clase_jugador.rect.height))
    # Actualizar la pantalla

    clase_jugador.do_movement(letras_precionadas,lista_de_eventos)
    clase_jugador.update()
    bullets.update()
    bullets.draw(screen)

    pygame.display.update()
    clock.tick(fps)
# Salir de Pygame
pygame.quit()
sys.exit()


