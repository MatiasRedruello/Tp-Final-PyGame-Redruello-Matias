import pygame
import sys
from clase_proyectil import Proyectil
from clase_jugador import Jugador
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
lista_enemigos = []
caracteristicas = Archivo.crear_lista_caracteristicas("info.json","r","nivel_uno","enemigo")

for diccionario_enemigo in caracteristicas:
    print(diccionario_enemigo)
    enemigo = Enemy(diccionario_enemigo.get("rect_speed_x"),diccionario_enemigo.get("rect_speed_y"),diccionario_enemigo.get("rect_width"),diccionario_enemigo.get("rect_height"),
                    diccionario_enemigo.get("inicial_x"),diccionario_enemigo.get("inicial_y"),diccionario_enemigo.get("pixel_limit_rigth"),
                    diccionario_enemigo.get("pixel_limit_left"),diccionario_enemigo.get("pixel_limit_y"),diccionario_enemigo.get("lado"))
    lista_enemigos.append(enemigo)
jugador = Jugador()
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
            nuevo_proyectil = Proyectil(jugador.rect.x, jugador.rect.y,
                                        jugador.rect.width,jugador.rect.height,True)
            sprites.add(nuevo_proyectil)
        # Detecta si se preciono la tecla de disparo a la izquierda  
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a and not event.key == pygame.K_d:
            nuevo_proyectil = Proyectil(jugador.rect.x,jugador.rect.y,
                                        jugador.rect.width,jugador.rect.height,False)
            sprites.add(nuevo_proyectil)            
        

    # Dibujar el fondo
    screen.blit(back_img, back_img.get_rect())  # Color blanco como fondo

    # Dibujar el rectángulo en su nueva posición

    pygame.draw.rect(screen, (255,0,0),(jugador.rect.x, jugador.rect.y, jugador.rect.width, jugador.rect.height))
    # Actualizar la pantalla
        #Actualizar enemigos
    for new_enemy in lista_enemigos:
        pygame.draw.rect(screen, (0,255,0),(new_enemy.rect.x, new_enemy.rect.y, new_enemy.rect.width, new_enemy.rect.height))
        new_enemy.do_movement()
        new_enemy.update()

    #Actualizar Jugador
    jugador.do_movement(letras_precionadas,lista_de_eventos)
    jugador.update()

    sprites.update()
    sprites.draw(screen)

    pygame.display.update()
    clock.tick(fps)
# Salir de Pygame
pygame.quit()
sys.exit()



