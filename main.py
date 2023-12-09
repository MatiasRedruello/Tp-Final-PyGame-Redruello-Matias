import pygame
import sys
from clase_screeen import Screen_settings
from clase_sprite_interactions import Sprite_interactions
from GUI_menu_principal import PrimerMenu
from GUI_seleccion_nivel import SeleccionNivel


pygame.init()

# Configuración de la ventana
screen_setup = Screen_settings()# Dejalo ahi porque explota
screen = pygame.display.set_mode((screen_setup.screen_width, screen_setup.screen_height))
pygame.display.set_caption('Salto de un Rectángulo')


#clock
clock = pygame.time.Clock()
fps = 60

#tipo y tamaño de funete del tiempo
font = pygame.font.Font(None, 100)
you_lose_font = pygame.font.Font(None, 50)
you_win_font = pygame.font.Font(None, 50)
score_font= pygame.font.Font(None, 36)
#All Sprites and interactions
sprite_groups = Sprite_interactions(screen_setup.screen_width,screen_setup.screen_height,screen)

#Flags
running_game = False
you_lose_flag = False
you_win_game_flag = False


start_time = pygame.time.get_ticks()
primer_menu = PrimerMenu(screen)
level_selection  = SeleccionNivel(screen)

while primer_menu.running:
    clicked = primer_menu.check_events()
    screen.fill((0, 0, 0))  # Limpia la pantalla en cada iteración
    primer_menu.draw()
    pygame.display.update()

    if clicked == "start_game":
        primer_menu.running = False
        level_selection.running = True

        while level_selection.running:
            load_level = level_selection.check_events()
            sprite_groups.current_level = load_level
            if load_level == "level_one":
                sprite_groups.current_level = "level_one"
                break
            #controlo que si eligen nivel dos o tres tener lo requisitos necesario para que no rompa
            elif load_level == "level_two": 
                sprite_groups.current_level = "level_one" #Tiene que estar asi por la condicion de entrada al siguiente nivel
                # sprite_groups.portal.inside_the_portal == True
                level_selection.force_level = True
                break
            elif  load_level == "level_three":
                sprite_groups.current_level = "level_two" #Tiene que estar asi por la condicion de entrada al siguiente nivel
                # sprite_groups.portal.inside_the_portal == True
                level_selection.force_level = True
                break

            elif load_level is not None:
                # Lógica para iniciar el juego con el nivel seleccionado
                running_game = False
                # Aquí puedes usar el valor de selected_level para determinar qué nivel cargar
                # Luego, iniciar el juego con ese nivel  
            screen.fill((0, 0, 0))
            level_selection.draw()
            pygame.display.update()
            running_game = True
                   
    elif clicked == "Exit":
        running_game = False
        pygame.quit()
    
    
       


while running_game:
    
    tiempo_control = 3
    tiempo = pygame.time.get_ticks() - start_time
    letras_precionadas = pygame.key.get_pressed()
    lista_de_eventos = pygame.event.get()
    delta_ms = clock.tick(fps)
    # le resto al minuto el tiempo, USO MAX Y EL MINO EN 0 PARA QUE NO ME DE NUEMERO NEGATIVO
    contador = max(0, 60000 - tiempo) // 1000 
    

    # Sección de selección de nivel

              
    # pasar de un nivel a otro
    if (sprite_groups.current_level == "level_one" and sprite_groups.portal.inside_the_portal == True) or \
        (sprite_groups.current_level == "level_one" and level_selection.force_level):
        sprite_groups.current_level = "level_two"
        screen_setup.current_level = "level_two"
        
        sprite_groups.level_config()
        screen_setup.level_config()
        start_time = pygame.time.get_ticks()
        sprite_groups.portal.inside_the_portal = False
        level_selection.force_level = False
        
        screen_setup.update()
    elif (sprite_groups.current_level == "level_two"  and sprite_groups.portal.inside_the_portal == True) or \
        (sprite_groups.current_level == "level_two" and level_selection.force_level):
        sprite_groups.current_level = "level_three"
        screen_setup.current_level = "level_three"

        sprite_groups.level_config()
        screen_setup.level_config()
        start_time = pygame.time.get_ticks()
        sprite_groups.portal.inside_the_portal = False
        you_win_game_flag = True
        screen_setup.update()
        
    # Formas de terminal el juego
    for event in lista_de_eventos:
        if event.type == pygame.QUIT:
            running_game = False  
    # Quedarse sin tiempo o morir
    if contador == 0 or sprite_groups.game_over:
        you_lose_flag = True
        # Renderizar mensaje 
        you_lose_surface = you_lose_font.render(f"GAME OVER", True, (255, 0, 0))  # Color blanco
        # Obtener rectángulo del texto renderizado
        you_lose_rect = you_lose_surface.get_rect()
        # si no gano en un minuto
        you_lose_rect.center = (screen_setup.screen_width // 2, screen_setup.screen_height//2-20)
    # Ganar el juego
    if you_win_game_flag:
        you_win_surface = you_win_font.render(f"YOU WIN", True, (255, 0, 0))  # Color blanco
        # Obtener rectángulo del texto renderizado
        you_win_rect = you_win_surface.get_rect()
        # si no gano en un minuto
        you_win_rect.center = (screen_setup.screen_width // 2, screen_setup.screen_height//2-20)


    #Mostrar contador por pantalla
    # Renderizar tiempo restante
    tiempo_surface = font.render(f"{contador}", True, (255, 255, 0))  # Color blanco
    # Obtener rectángulo del texto renderizado
    tiempo_rect = tiempo_surface.get_rect()
    # Centrar el texto en la parte superior de la pantalla
    tiempo_rect.midtop = (screen_setup.screen_width // 2, 10)  # Mitad superior de la pantalla


    # Draw background
    screen.blit(screen_setup.transform_back_img, screen_setup.transform_back_img.get_rect())  # Color blanco como fondo
    screen.blit(tiempo_surface, tiempo_rect)

    if you_lose_flag:
        screen.blit(you_lose_surface, you_lose_rect)  
        if tiempo//1000 == 63 or tiempo//1000 - sprite_groups.defuntion_time//1000 ==3:
            running_game = False

    if you_win_game_flag:
        screen.blit(you_win_surface, you_win_rect)  
        if tiempo//1000 == 63 or tiempo//1000 - sprite_groups.defuntion_time//1000 ==3:
            running_game = False    
     
   
    score_text = score_font.render(f"Score: {sprite_groups.player.score}", True, (255, 255, 255))
    score_rect = score_text.get_rect()
    score_rect.midtop = (screen_setup.screen_width // 2, tiempo_rect.bottom + 10)  # Alinea el puntaje debajo del tiempo
    screen.blit(score_text, score_rect)        
        

    if sprite_groups.player.alive:
        
        sprite_groups.delta_ms = delta_ms
        sprite_groups.time = tiempo
        sprite_groups.time_left = contador
        sprite_groups.lista_de_eventos = lista_de_eventos
        sprite_groups.letras_precionadas = letras_precionadas
        sprite_groups.draw()
        sprite_groups.update()

    pygame.display.update()
    
# Salir de Pygame
pygame.quit()
sys.exit()




