import pygame
from pygame.sprite import AbstractGroup
from clase_archivo import Archivo
screen_width = 800
screen_height = 600


# Color y dimensiones del rectángulo(podrian se rpropertys de una clase)
rect_color = (0, 0, 255)  # Azul en formato RGB
rect_width = 50
rect_height = 50

"""x = 0
y = screen_height - rect_height"""
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
        self.rect = pygame.Rect(self.inicial_x, self.inicial_y, self.rect_width, self.rect_height)   
        self.proyectil = self.archivo_json.get("player").get("proyectil")  
        self.lado = True
        self.jump_height = 15
        self.gravity = 1
        self.jumping = False
        self.screen_width = screen_width
        self.screen_height = screen_height
    def jump_settings(self):

        self.rect_speed_y += self.gravity
        self.rect.y += self.rect_speed_y
        # Controlar el salto
        if self.rect.y >= screen_height - self.rect.height:
            self.rect.y = screen_height - self.rect.height
            self.jumping = False
            self.rect_speed_y = 0  
    
    def do_walk(self,letras_precionadas):
        if letras_precionadas[pygame.K_RIGHT] and not letras_precionadas[pygame.K_LEFT]:
            self.rect.x += self.rect_speed_x
            #Limite de movimiento derecho
            if self.rect.x > screen_width-self.rect_width:
                self.rect.x += -self.rect_speed_x
        elif letras_precionadas[pygame.K_LEFT] and not letras_precionadas[pygame.K_RIGHT]:
            self.rect.x += -self.rect_speed_x
            # Limite de movimiento izquierdo
            if self.rect.x < 0:
                self.rect.x += self.rect_speed_x

    def do_jump(self,lista_de_eventos):
        # Detecta la tecla de espacio para activar el salto
        for event in lista_de_eventos:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not self.jumping:
                self.jumping = True
                self.rect_speed_y = - self.jump_height  # Configura la velocidad inicial del salto
        self.jump_settings()

      

    def do_movement(self,letras_precionadas,lista_de_eventos):
        self.do_walk(letras_precionadas)
        self.do_jump(lista_de_eventos)
        
    def update(self):
         pass
          





