import pygame
from clase_archivo import File


"""x = 0
y = screen_height - rect_height"""
class Portal(pygame.sprite.Sprite):
    def __init__(self,
                screen_width,
                screen_height) -> None:
        super().__init__()
        # Caracteristicas
        self.portal_path = r"Portal/furniture_door_door_door_up_x1_1_png_1354837638.png"
        self.portal_image = pygame.image.load(self.portal_path)
        self.portal_image = pygame.transform.scale(self.portal_image, (50, 80))
        self.inicial_x = 0 
        self.inicial_y = 0
        self.image = self.portal_image # Heredo de sprite
        self.rect = self.portal_image.get_rect()
        self.rect.topleft = (self.inicial_x, self.inicial_y) 


    def update(self):
         pass
          





