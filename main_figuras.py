import pygame
import sys
from clase_proyectil import Proyectil
pygame.init()

# Configuración de la ventana
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Salto de un Rectángulo')

back_img = pygame.image.load("background\goku_house.png")# Cargo imagen de fondo
back_img = pygame.transform.scale(back_img, (screen_width, screen_height))#Adapto imagen a la pantalla 

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

# Color y dimensiones del rectángulo(podrian se rpropertys de una clase)
rect_color = (0, 0, 255)  # Azul en formato RGB
rect_width = 50
rect_height = 50



# Lista para almacenar los proyectiles
bullets = pygame.sprite.Group()

# Posición y velocidad inicial del rectángulo(podrian se rpropertys de una clase)
x = 0
y = screen_height - rect_height
rect_speed_y = 0  # Velocidad inicial en el eje Y
rect_speed_x = 10

gravity = 1  # Fuerza de gravedad
jump_height = 15  # Altura máxima del salto

# Color y dimensiones del proyectil(podria ser propertys de una clase)

#clock
clock = pygame.time.Clock()
fps = 60

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
            shooting = True
            nuevo_proyectil = Proyectil(x, y,True)
            bullets.add(nuevo_proyectil)
        # Detecta si se preciono la tecla de disparo a la izquierda  
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            shooting = True
            nuevo_proyectil = Proyectil(x, y,False)
            bullets.add(nuevo_proyectil)            
        
    # Movimiento a la izquierda
    if letras_precionadas[pygame.K_RIGHT] and not letras_precionadas[pygame.K_LEFT]:
        x += rect_speed_x
        #Limite de movimiento derecho
        if x > screen_width-rect_width:
            x += -rect_speed_x
    # Movimiento a la derecha
    if letras_precionadas[pygame.K_LEFT] and not letras_precionadas[pygame.K_RIGHT]:
        x += -rect_speed_x
        # Limite de movimiento izquierdo
        if x < 0:
            x += rect_speed_x
    # Simular la gravedad
    rect_speed_y += gravity
    y += rect_speed_y

    # Controlar el salto
    if y >= screen_height - rect_height:
        y = screen_height - rect_height
        jumping = False
        rect_speed_y = 0  # Reinicia la velocidad vertical si toca el suelo
    

    # Dibujar el fondo
    screen.blit(back_img, back_img.get_rect())  # Color blanco como fondo

    # Dibujar el rectángulo en su nueva posición
    pygame.draw.rect(screen, (255,0,0), (x, y, rect_width, rect_height))
    # Actualizar la pantalla
    bullets.update()
    bullets.draw(screen)

    pygame.display.update()
    clock.tick(fps)
# Salir de Pygame
pygame.quit()
sys.exit()
