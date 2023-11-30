import pygame
import sys
from clase_screeen import Screen_settings
from clase_sprite_interactions import Sprite_interactions

pygame.init()

# Configuración de la ventana
screen_setup = Screen_settings()# Dejalo ahi porque explota
screen = pygame.display.set_mode((screen_setup.screen_width, screen_setup.screen_height))
pygame.display.set_caption('Salto de un Rectángulo')

#clock
clock = pygame.time.Clock()
fps = 60

#All Sprites and interactions
sprite_groups = Sprite_interactions(screen_setup.screen_width,screen_setup.screen_height,screen)

#Flags
running_game = True

while running_game:
    tiempo = pygame.time.get_ticks()
    letras_precionadas = pygame.key.get_pressed()
    lista_de_eventos = pygame.event.get()
    delta_ms = clock.tick(fps)
    for event in lista_de_eventos:
        if event.type == pygame.QUIT:
            running_game = False    

    # Draw background
    screen.blit(screen_setup.transform_back_img, screen_setup.transform_back_img.get_rect())  # Color blanco como fondo

    sprite_groups.delta_ms = delta_ms
    sprite_groups.time = tiempo
    sprite_groups.lista_de_eventos = lista_de_eventos
    sprite_groups.letras_precionadas = letras_precionadas
    sprite_groups.draw()
    sprite_groups.update()



    pygame.display.update()
    
# Salir de Pygame
pygame.quit()
sys.exit()




