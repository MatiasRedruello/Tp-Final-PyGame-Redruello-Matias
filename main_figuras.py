import pygame
import sys
from clase_proyectil import Proyectil
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
sprites = pygame.sprite.Group()

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
# Crear jugador
player = Player(screen_width,screen_height)
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
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d and not event.key == pygame.K_a :
            nuevo_proyectil = Proyectil(player.rect.x,player.rect.y,
                                        player.rect.width,player.rect.height,player.proyectil.get("bullet_path"),
                                        player.proyectil.get("bullet_width"),player.proyectil.get("bullet_height"),
                                        player.proyectil.get("bullet_speed"),True)
            sprites.add(nuevo_proyectil)
        # Detecta si se preciono la tecla de disparo a la izquierda  
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a and not event.key == pygame.K_d:
            nuevo_proyectil = Proyectil(player.rect.x,player.rect.y,
                                        player.rect.width,player.rect.height,player.proyectil.get("bullet_path"),
                                        player.proyectil.get("bullet_width"),player.proyectil.get("bullet_height"),
                                        player.proyectil.get("bullet_speed"),False)
            sprites.add(nuevo_proyectil)        

    # Dibujar el fondo
    screen.blit(back_img, back_img.get_rect())  # Color blanco como fondo

    # Dibujar el rectángulo en su nueva posición

    pygame.draw.rect(screen, (255,0,0),(player.rect.x, player.rect.y, player.rect.width, player.rect.height))
    # Actualizar la pantalla
        #Actualizar enemigos
    for new_enemy in enemy_list:
        pygame.draw.rect(screen, (0,255,0),(new_enemy.rect.x, new_enemy.rect.y, new_enemy.rect.width, new_enemy.rect.height))
        nuevo_proyectil_enemigo = Proyectil(new_enemy.rect.x,new_enemy.rect.y,
                                        new_enemy.rect.width,new_enemy.rect.height,"Power/gema_roja.png",
                                        10,10,
                                        5,False)
        sprites.add(nuevo_proyectil_enemigo)
        new_enemy.do_movement()
        new_enemy.update()

    #Actualizar Jugador
    player.do_movement(letras_precionadas,lista_de_eventos)
    player.update()

    sprites.update()
    sprites.draw(screen)

    pygame.display.update()
    clock.tick(fps)
# Salir de Pygame
pygame.quit()
sys.exit()



