import pygame



class Item(pygame.sprite.Sprite):
    def __init__(self,inicial_x,
                inicial_y,) -> None:
        super().__init__()
        # Caracteristicas
        self.item_path = "Item/pile_of_currants__x1_1_png_1354840042.png"
        self.item_image = pygame.image.load(self.item_path)
        
        self.inicial_x = inicial_x 
        self.inicial_y = inicial_y
        self.image = self.item_image # Heredo de sprite
        self.rect = self.item_image.get_rect()
        self.rect.topleft = (self.inicial_x, self.inicial_y)      
        #cuando tenga el sprite va a servir 


    def update(self):
         pass
          





