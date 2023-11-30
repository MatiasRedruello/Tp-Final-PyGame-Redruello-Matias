import pygame
from clase_archivo import File

class Screen_settings():
    def __init__(self) -> None:
        self.settings = File.json_load("info.json","r","settings")
        self.screen_width = self.settings.get("screen").get("screen_width") 
        self.screen_height = self.settings.get("screen").get("screen_height")
        self.back_img = pygame.image.load(self.settings.get("screen").get("background_level_one"))
        self.transform_back_img = pygame.transform.scale(self.back_img, (self.screen_width, self.screen_height))