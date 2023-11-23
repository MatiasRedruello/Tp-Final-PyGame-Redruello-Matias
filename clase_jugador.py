import pygame
from pygame.sprite import AbstractGroup
from clase_archivo import Archivo
from clase_proyectil import Proyectil

class Player(pygame.sprite.Sprite):
    def __init__(self,screen_width,screen_height) -> None:
        super().__init__()
        # Caracteristicas
        self.archivo_json = Archivo.leer_json("info.json","r","level_one")
        self.rect_color = self.archivo_json.get("player").get("rect_color")
        self.rect_speed_x = self.archivo_json.get("player").get("rect_speed_x") # set
        self.rect_speed_y = self.archivo_json.get("player").get("rect_speed_y") # set
        self.rect_width = self.archivo_json.get("player").get("rect_width") 
        self.rect_height = self.archivo_json.get("player").get("rect_height")
        self.inicial_x = self.archivo_json.get("player").get("inicial_x") #Donde Inicia en x
        self.inicial_y = self.archivo_json.get("player").get("inicial_y") #Donde Inicia en y
        self.player_path = "Player/player_ship.png"
        self.player_image = pygame.image.load(self.player_path) 
        self.player_image = pygame.transform.scale(self.player_image, (self.rect_width, self.rect_height))
        self.image = self.player_image # Necesito si o si self image ¿,si no romple en la clase sprite, acapuedoescalar si quiero
        self.sprites = pygame.sprite.Group()  
        self.sprite_player = pygame.sprite.Sprite()  # Crear sprite del ítem
        self.sprite_player.image = self.player_image  # Asignar imagen al sprite
        self.sprite_player.rect = self.player_image.get_rect()
        self.sprite_player.rect.topleft = (self.inicial_x, self.inicial_y)
        self.proyectil = self.archivo_json.get("player").get("proyectil")  
        self.lado = True
        self.jump_height = 15
        self.gravity = 1
        self.jumping = False
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.sprites = pygame.sprite.Group()
        self.ultimo_disparo = 0
        self.timepo_control = 500  
        

    def jump_settings(self):

        self.rect_speed_y += self.gravity
        self.sprite_player.rect.y += self.rect_speed_y
        # Controlar el salto
        if self.sprite_player.rect.y > self.screen_height - self.sprite_player.rect.height:
            self.sprite_player.rect.y = self.screen_height - self.sprite_player.rect.height
            self.jumping = False # reinicio el salto, si no slata una sola vez
            
    
    def do_walk(self,letras_precionadas):
        if letras_precionadas[pygame.K_RIGHT] and not letras_precionadas[pygame.K_LEFT]:
            self.sprite_player.rect.x += self.rect_speed_x
            #Limite de movimiento derecho
            if self.sprite_player.rect.x > self.screen_width-self.rect_width:
                self.sprite_player.rect.x += -self.rect_speed_x
        elif letras_precionadas[pygame.K_LEFT] and not letras_precionadas[pygame.K_RIGHT]:
            self.sprite_player.rect.x += -self.rect_speed_x
            # Limite de movimiento izquierdo
            if self.sprite_player.rect.x < 0:
                self.sprite_player.rect.x += self.rect_speed_x

    def do_jump(self,lista_de_eventos):
        # Detecta la tecla de espacio para activar el salto
        for event in lista_de_eventos:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not self.jumping:
                self.jumping = True # me evita el salto multiple
                self.rect_speed_y = - self.jump_height  # Configura la velocidad inicial del salto
        self.jump_settings()

    def do_shoot(self,lista_de_eventos,tiempo_actual):
        for event in lista_de_eventos:   
            if tiempo_actual-self.ultimo_disparo > self.timepo_control:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_d and not event.key == pygame.K_a :
                    nuevo_proyectil = Proyectil(self.sprite_player.rect.x,self.sprite_player.rect.y,
                                                self.sprite_player.rect.width,self.sprite_player.rect.height,self.proyectil.get("bullet_path"),
                                                self.proyectil.get("bullet_width"),self.proyectil.get("bullet_height"),
                                                self.proyectil.get("bullet_speed"),True)
                    self.sprites.add(nuevo_proyectil)
                    self.ultimo_disparo = tiempo_actual

            if tiempo_actual-self.ultimo_disparo > self.timepo_control:        
                # Detecta si se preciono la tecla de disparo a la izquierda  
                if event.type == pygame.KEYDOWN and event.key == pygame.K_a and not event.key == pygame.K_d:
                    nuevo_proyectil = Proyectil(self.sprite_player.rect.x,self.sprite_player.rect.y,
                                                self.sprite_player.rect.width,self.sprite_player.rect.height,self.proyectil.get("bullet_path"),
                                                self.proyectil.get("bullet_width"),self.proyectil.get("bullet_height"),
                                                self.proyectil.get("bullet_speed"),False)
                    self.sprites.add(nuevo_proyectil)          
                    self.ultimo_disparo = tiempo_actual

    def do_movement(self,letras_precionadas,lista_de_eventos,tiempo_actual):
        self.do_walk(letras_precionadas)
        self.do_jump(lista_de_eventos)
        self.do_shoot(lista_de_eventos,tiempo_actual)
        
    def update(self):
         pass
          





