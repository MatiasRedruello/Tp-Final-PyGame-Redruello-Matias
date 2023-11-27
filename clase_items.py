import pygame



class Item(pygame.sprite.Sprite):
    def __init__(self,inicial_x,
                inicial_y,item_path) -> None:
        super().__init__()
        # Caracteristicas
        self.inicial_x = inicial_x 
        self.inicial_y = inicial_y
        self.item_image = pygame.image.load(item_path)        
        self.image = self.item_image # Heredo de sprite
        self.rect = self.item_image.get_rect()
        self.rect.topleft = (self.inicial_x, self.inicial_y)      
        #cuando tenga el sprite va a servir 


    def update(self):
         pass
          





