import pygame
from pygame.sprite import AbstractGroup
from clase_archivo import File
from clase_proyectil import Bullet
from clase_auxiliar import Suport


"""x = 0
y = screen_height - rect_height"""
class Plataforma(pygame.sprite.Sprite):
    def __init__(self,rect_speed_x,rect_speed_y,
                inicial_x  , 
                inicial_y  ,
                pixel_limit_rigth,
                pixel_limit_left,
                lado,plataform_path,plataform_scale) -> None:
        super().__init__()
        # Caracteristicas
        self.rect_speed_x = rect_speed_x # set
        self.rect_speed_y = rect_speed_y # set

        self.inicial_x = inicial_x #Donde Inicia en x
        self.inicial_y = inicial_y #Donde Inicia en y
        self.item_image = pygame.image.load(plataform_path)        
        self.image = pygame.transform.scale(self.item_image,plataform_scale) # Heredo de sprite
        self.rect = self.item_image.get_rect()
        self.rect.topleft = (self.inicial_x, self.inicial_y)    
        self.lado = lado
        self.pixel_limit_rigth = pixel_limit_rigth #set
        self.pixel_limit_left = pixel_limit_left #set
        self.sprites = pygame.sprite.Group()

    def do_walk(self):
        # Movimiento horizontal
        if self.lado == "True":
            self.rect.x += self.rect_speed_x
            # Limitar el movimiento a la derecha
            if self.rect.right > 1000 - self.pixel_limit_rigth:# el valor maximo de panalla - los pixeles donde es ellimite
                self.rect.right = 1000 - self.pixel_limit_rigth# lo tenes que ubicar en el mismo lugar que el cuadrado apra que no desaparece
                self.lado = "False"  # Cambia la dirección
        elif self.lado == "False":
            self.rect.x -= self.rect_speed_x
            # Limitar el movimiento a la izquierda
            if self.rect.left < 0 + self.pixel_limit_left: # el valor maximo de panalla - los pixeles donde es ellimite
                self.rect.left = 0 + self.pixel_limit_left # lo tenes que ubicar en el mismo lugar que el cuadrado apra que no desaparece
                self.lado = "True"  # Cambia la dirección         
    
    def do_movement(self):
        self.do_walk()


        
    def update(self):
         pass
          





