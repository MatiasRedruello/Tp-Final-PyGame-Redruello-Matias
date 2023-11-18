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



# Color y dimensiones del rectángulo(podrian se rpropertys de una clase)
rect_color = (0, 0, 255)  # Azul en formato RGB
rect_width = 50
rect_height = 50



# Lista para almacenar los proyectiles
bullets = pygame.sprite.Group()

# Posición y velocidad inicial del rectángulo(podrian se rpropertys de una clase)

rect_speed_y = 0  # Velocidad inicial en el eje Y
rect_speed_x = 10

gravity = 1  # Fuerza de gravedad
jump_height = 15  # Altura máxima del salto

# Color y dimensiones del proyectil(podria ser propertys de una clase)

#clock
clock = pygame.time.Clock()
fps = 60
clase_jugador = Jugador()
# Bucle principal del juego

jumping = False
shooting = False 
running_game = True

while running_game:
    letras_precionadas = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_game = False

        # Detecta la tecla de espacio para activar el salto
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not jumping:
            jumping = True
            rect_speed_y = -jump_height  # Configura la velocidad inicial del salto
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
        
    # Movimiento a la izquierda
    

    # Mov
    # Simular la gravedad
    rect_speed_y += gravity
    clase_jugador.rect.y += rect_speed_y

    # Controlar el salto
    if clase_jugador.rect.y >= screen_height - clase_jugador.rect.height:
        clase_jugador.rect.y = screen_height - clase_jugador.rect.height
        jumping = False
        rect_speed_y = 0  # Reinicia la velocidad vertical si toca el suelo
    

    # Dibujar el fondo
    screen.blit(back_img, back_img.get_rect())  # Color blanco como fondo

    # Dibujar el rectángulo en su nueva posición
    pygame.draw.rect(screen, (255,0,0),(clase_jugador.rect.x, clase_jugador.rect.y, clase_jugador.rect.width, clase_jugador.rect.height))
    # Actualizar la pantalla

    clase_jugador.do_movement(letras_precionadas)
    clase_jugador.update()
    bullets.update()
    bullets.draw(screen)

    pygame.display.update()
    clock.tick(fps)
# Salir de Pygame
pygame.quit()
sys.exit()


