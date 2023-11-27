import pygame
import sys
from clase_jugador import Player
from clase_enemigo import Enemy
from clase_archivo import File
from clase_plataforma import Plataforma
from clase_portal import Portal
from clase_items import Item
pygame.init()

# Configuración de la ventana
settings = File.json_load("info.json","r","settings")

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

#crear lista de items
item_list = []
item_porperty = File.create_property_list("info.json","r","level_one","items")
for item_dict in item_porperty:
    item = Item(item_dict.get("inicial_x"),item_dict.get("inicial_y"),item_dict.get("item_path"))
    item_list.append(item)
    
#plataformas
plataforma_list = []
plataforma_porperty = File.create_property_list("info.json","r","level_one","plataforma")
for plataforma_dict in plataforma_porperty:
    plataforma = Plataforma(plataforma_dict.get("rect_speed_x"),plataforma_dict.get("rect_speed_y"),
                    plataforma_dict.get("inicial_x"),plataforma_dict.get("inicial_y"),plataforma_dict.get("pixel_limit_rigth"),
                    plataforma_dict.get("pixel_limit_left"),plataforma_dict.get("lado"),
                    plataforma_dict.get("plataform_path"),plataforma_dict.get("plataform_scale"))
    plataforma_list.append(plataforma)
# crea lista enemigos
enemy_list = []
enemy_property = File.create_property_list("info.json","r","level_one","enemigo")
for enemy_dict in enemy_property:
    enemy = Enemy(enemy_dict.get("rect_speed_x"),enemy_dict.get("rect_speed_y"),
                    enemy_dict.get("inicial_x"),enemy_dict.get("inicial_y"),enemy_dict.get("pixel_limit_rigth"),
                    enemy_dict.get("pixel_limit_left"),enemy_dict.get("pixel_limit_y"),enemy_dict.get("bullet_path"),
                    enemy_dict.get("walk_path"),
                    enemy_dict.get("row"),enemy_dict.get("colum"))
    enemy_list.append(enemy)
sprites = pygame.sprite.Group()    
# Crear jugador
player = Player(screen_width,screen_height)
portal = Portal()
# Bucle principal del juego


shooting = False 
running_game = True

while running_game:
    tiempo = pygame.time.get_ticks()
    letras_precionadas = pygame.key.get_pressed()
    lista_de_eventos = pygame.event.get()
    delta_ms = clock.tick(fps)
    for event in lista_de_eventos:
        if event.type == pygame.QUIT:
            running_game = False

    # Dibujar el fondo
    screen.blit(back_img, back_img.get_rect())  # Color blanco como fondo

    # Dibujar el rectángulo en su nueva posición (el jugador)d 
     # Dibujar el rectángulo en su nueva posición (el portal)
    

    for new_item in item_list:
        sprites.add(new_item)
        new_item.update()

    for new_plataforma in plataforma_list:
        sprites.add(new_plataforma)
        #sprites.add(new_plataforma.sprites)# si lo saco no se ve el sprite del shoot del enemigo
        new_plataforma.do_movement()
        new_plataforma.update()  

        #Actualizar enemigos
    for new_enemy in enemy_list:
        sprites.add(new_enemy.bullets_group,new_enemy)# si lo saco no se ve el sprite del shoot del enemigo
        new_enemy.do_movement(tiempo,delta_ms)
        new_enemy.update()
    portal.do_animation(delta_ms)
    sprites.add(player,player.bullets_group,portal)   

    #Actualizar Jugador
    player.do_movement(letras_precionadas,lista_de_eventos,tiempo,delta_ms)
  
    sprites.update()
    sprites.draw(screen)

    pygame.display.update()
    
# Salir de Pygame
pygame.quit()
sys.exit()



