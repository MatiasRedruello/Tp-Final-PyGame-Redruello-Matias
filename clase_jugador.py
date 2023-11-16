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
rect_speed_y = 0  # Velocidad inicial en el eje Y
rect_speed_x = 10




class Jugador(pygame.sprite.Sprite):
    def __init__(self,x,y,lado= True) -> None:
        super().__init__()
        self.rect_width = 50
        self.rect_height = 50
        self.inicial_x = 0
        self.inicial_y = 500
        self.rect = pygame.Rect(self.inicial_x, self.inicial_y, self.rect_width, self.rect_height)       
        self.lado = lado

    def do_move(self):
        if self.lado:
            self.inicial_x += rect_speed_x
            #Limite de movimiento derecho
            if self.inicial_x > screen_width-rect_width:
                self.inicial_x += -rect_speed_x
        elif self.lado == False:
            self.inicial_x += -rect_speed_x
            # Limite de movimiento izquierdo
            if self.inicial_x < 0:
                self.inicial_x += rect_speed_x

    def update(self):
        self.do_move()    





