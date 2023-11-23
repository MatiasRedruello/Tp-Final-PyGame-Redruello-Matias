import pygame
from pygame.sprite import AbstractGroup
from clase_archivo import Archivo


class Item(pygame.sprite.Sprite):
    def __init__(self,inicial_x,
                inicial_y,) -> None:
        super().__init__()
        # Caracteristicas
        self.item_path = "Power/gema_roja.png"
        self.item_image = pygame.image.load(self.item_path)
        self.inicial_x = inicial_x 
        self.inicial_y = inicial_y
        self.image = self.item_image # Necesito si o si self image ¿,si no romple en la clase sprite, acapuedoescalar si quiero
        self.sprites = pygame.sprite.Group()  
        self.sprite_item = pygame.sprite.Sprite()  # Crear sprite del ítem
        self.sprite_item.image = self.item_image  # Asignar imagen al sprite
        self.sprite_item.rect = self.item_image.get_rect()
        self.sprite_item.rect.topleft = (self.inicial_x, self.inicial_y)
        self.sprites.add(self.sprite_item)      
        #cuando tenga el sprite va a servir 


    def update(self):
         pass
          





