import pygame
from clase_archivo import File

class Screen_settings():
    def __init__(self) -> None:
        self.current_level = "level_one"
        self.level_config()
       

    def level_config(self):
        self.settings = File.json_load("info.json","r",self.current_level)
        self.screen_width = self.settings.get("screen").get("screen_width") 
        self.screen_height = self.settings.get("screen").get("screen_height")
        self.back_img = pygame.image.load(self.settings.get("screen").get("background_level"))
        self.transform_back_img = pygame.transform.scale(self.back_img, (self.screen_width, self.screen_height))

    def update(self):
        pass