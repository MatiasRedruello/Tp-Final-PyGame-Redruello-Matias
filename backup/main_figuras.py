import pygame
import sys

pygame.init()

# Configuración de la ventana
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Salto de un Rectángulo')

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

# Color y dimensiones del rectángulo(podrian se rpropertys de una clase)
rect_color = (0, 0, 255)  # Azul en formato RGB
rect_width = 50
rect_height = 50

bullet_image = pygame.image.load('Power/gema_roja.png')
bullet_width = 30
bullet_height = 15

class Proyectil(pygame.sprite.Sprite):
    def __init__(self, x, y,lado):
        super().__init__()
        self.image = pygame.transform.scale(bullet_image, (bullet_width, bullet_height))
        self.rect = self.image.get_rect()
        self.rect.center = (x+(rect_width//2), y+(rect_height//2))
        self.speed_x = 5
        self.lado = lado
    def update(self):
        if self.lado == "rigth":
            self.rect.x += self.speed_x
        elif self.lado == "left":
            self.rect.x += -self.speed_x



# Lista para almacenar los proyectiles
bullets = pygame.sprite.Group()

# Posición y velocidad inicial del rectángulo(podrian se rpropertys de una clase)
x = screen_width // 2 - rect_width // 2
y = screen_height - rect_height
rect_speed_y = 0  # Velocidad inicial en el eje Y
rect_speed_x = 10

gravity = 1  # Fuerza de gravedad
jump_height = 15  # Altura máxima del salto

# Color y dimensiones del proyectil(podria ser propertys de una clase)
bullet_color = red  # Rojo en formato RGB
bullet_x = 0
bullet_y = 0
bullet_width = 10
bullet_height = 10
bullet_speed_x = 0

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
            nuevo_proyectil = Proyectil(x, y,"rigth")
            bullets.add(nuevo_proyectil)
        # Detecta si se preciono la tecla de disparo a la izquierda  
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            shooting = True
            nuevo_proyectil = Proyectil(x, y,"left")
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
    screen.fill((255, 255, 255))  # Color blanco como fondo

    # Dibujar el rectángulo en su nueva posición
    pygame.draw.rect(screen, rect_color, (x, y, rect_width, rect_height))
    # Actualizar la pantalla
    bullets.update()
    bullets.draw(screen)

    pygame.display.update()
    clock.tick(fps)
# Salir de Pygame
pygame.quit()
sys.exit()
