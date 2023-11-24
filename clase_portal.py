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
        self.json_file = File.json_load("info.json","r","level_one")
        self.rect_width = self.json_file.get("portal").get("rect_width")
        self.rect_height = self.json_file.get("portal").get("rect_height")
        self.inicial_x = self.json_file.get("portal").get("inicial_x") #Donde Inicia en x
        self.inicial_y = self.json_file.get("portal").get("inicial_y") #Donde Inicia en y
        self.rect = pygame.Rect(self.inicial_x, self.inicial_y, self.rect_width, self.rect_height)   
        self.screen_width = screen_width   
        self.screen_height = screen_height
        self.sprites = pygame.sprite.Group()#cuando tenga el sprite va a servir 


    def update(self):
         pass
          





