import pygame
from pygame.sprite import AbstractGroup

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Salto de un Rectángulo')

# Color y dimensiones del rectángulo(podrian se rpropertys de una clase)
rect_color = (0, 0, 255)  # Azul en formato RGB
rect_width = 50
rect_height = 50

"""x = 0
y = screen_height - rect_height"""
class Jugador(pygame.sprite.Sprite):
    def __init__(self,x=0,y=0,rect_speed_x = 10,rect_speed_y = 0,lado= True) -> None:
        super().__init__()
        # Caracteristicas
        self.rect_speed_x = rect_speed_x # set
        self.rect_speed_y = rect_speed_y # set
        self.rect_width = 50 
        self.rect_height = 50
        self.inicial_x = 0 #Donde Inicia en x
        self.inicial_y = 600 #Donde Inicia en y
        self.rect = pygame.Rect(self.inicial_x, self.inicial_y, self.rect_width, self.rect_height)       
        self.lado = lado
        self.jump_height = 15
        self.gravity = 1
        self.jumping = False

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
          





