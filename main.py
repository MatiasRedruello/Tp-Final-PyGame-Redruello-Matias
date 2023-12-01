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
font = pygame.font.Font(None, 100)#tipo y tamaño de funete del tiempo
you_lose_font = pygame.font.Font(None, 50)
#All Sprites and interactions
sprite_groups = Sprite_interactions(screen_setup.screen_width,screen_setup.screen_height,screen)
#Flags
running_game = True
you_lose_flag = False
while running_game:

    tiempo = pygame.time.get_ticks()
    letras_precionadas = pygame.key.get_pressed()
    lista_de_eventos = pygame.event.get()
    delta_ms = clock.tick(fps)
    # le resto al minuto el tiempo, USO MAX Y EL MINO EN 0 PARA QUE NO ME DE NUEMERO NEGATIVO
    tiempo_restante = max(0, 60000 - tiempo) // 1000 
    
    for event in lista_de_eventos:
        if event.type == pygame.QUIT:
            running_game = False  
    # Falta ver como mostrarlo por pantalla   
    if tiempo_restante == 0:
        you_lose_flag = True
        # Renderizar mensaje 
        you_lose_surface = you_lose_font.render(f"GAME OVER", True, (255, 0, 0))  # Color blanco
        # Obtener rectángulo del texto renderizado
        you_lose_rect = you_lose_surface.get_rect()
        # si no gano en un minuto
        you_lose_rect.center = (screen_setup.screen_width // 2, screen_setup.screen_height//2-20)


    #Mostrar contador por pantalla
    # Renderizar tiempo restante
    tiempo_surface = font.render(f"{tiempo_restante}", True, (255, 255, 0))  # Color blanco
    # Obtener rectángulo del texto renderizado
    tiempo_rect = tiempo_surface.get_rect()
    # Centrar el texto en la parte superior de la pantalla
    tiempo_rect.midtop = (screen_setup.screen_width // 2, 10)  # Mitad superior de la pantalla


    # Draw background
    screen.blit(screen_setup.transform_back_img, screen_setup.transform_back_img.get_rect())  # Color blanco como fondo
    screen.blit(tiempo_surface, tiempo_rect)

    if you_lose_flag:
        screen.blit(you_lose_surface, you_lose_rect)
        if tiempo//1000 == 63:
            running_game = False
        


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




