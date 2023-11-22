import pygame
import sys
from clase_jugador import Player
from clase_enemigo import Enemy
from clase_archivo import Archivo
pygame.init()

# Configuración de la ventana
settings = Archivo.leer_json("info.json","r","settings")

screen_width = settings.get("screen").get("screen_width") 
screen_height = settings.get("screen").get("screen_height")
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Salto de un Rectángulo')

back_img = pygame.image.load(settings.get("screen").get("background_level_one"))# Cargo imagen de fondo. set
back_img = pygame.transform.scale(back_img, (screen_width, screen_height))#Adapto imagen a la pantalla 

# Lista para almacenar los proyectiles


#clock
clock = pygame.time.Clock()
fps = 60

# crea lista enemigos
enemy_list = []
enemy_property = Archivo.crear_lista_caracteristicas("info.json","r","level_one","enemigo")
for enemy_dict in enemy_property:
    enemy = Enemy(enemy_dict.get("rect_speed_x"),enemy_dict.get("rect_speed_y"),enemy_dict.get("rect_width"),enemy_dict.get("rect_height"),
                    enemy_dict.get("inicial_x"),enemy_dict.get("inicial_y"),enemy_dict.get("pixel_limit_rigth"),
                    enemy_dict.get("pixel_limit_left"),enemy_dict.get("pixel_limit_y"),enemy_dict.get("lado"),
                    screen_width,screen_height)
    enemy_list.append(enemy)
sprites = pygame.sprite.Group()    
# Crear jugador
player = Player(screen_width,screen_height)
# Bucle principal del juego


shooting = False 
running_game = True

while running_game:
    tiempo = pygame.time.get_ticks()
    letras_precionadas = pygame.key.get_pressed()
    lista_de_eventos = pygame.event.get()

    for event in lista_de_eventos:
        if event.type == pygame.QUIT:
            running_game = False

    # Dibujar el fondo
    screen.blit(back_img, back_img.get_rect())  # Color blanco como fondo

    # Dibujar el rectángulo en su nueva posición

    pygame.draw.rect(screen, (255,0,0),(player.rect.x, player.rect.y, player.rect.width, player.rect.height))
    # Actualizar la pantalla
        #Actualizar enemigos
    for new_enemy in enemy_list:
        pygame.draw.rect(screen, (0,255,0),(new_enemy.rect.x, new_enemy.rect.y, new_enemy.rect.width, new_enemy.rect.height))
        sprites.add(new_enemy.sprites)
        new_enemy.do_movement(tiempo)
        new_enemy.update()

    sprites.add(player.sprites)   
    #Actualizar Jugador
    player.do_movement(letras_precionadas,lista_de_eventos,tiempo)
    player.update()

    sprites.update()
    sprites.draw(screen)

    pygame.display.update()
    clock.tick(fps)
# Salir de Pygame
pygame.quit()
sys.exit()



