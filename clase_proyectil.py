import pygame


bullet_image = pygame.image.load('Power/player_laser.png')#si json
bullet_width = 50#si json
bullet_height = 15#si json
rect_width =50# en este caso es del cuadrado del personaje
rect_height = 50## en este caso es del cuadrado del personaje

class Proyectil(pygame.sprite.Sprite):
    def __init__(self, x, y, lado= True):
        super().__init__()
        self.image = pygame.transform.scale(bullet_image, (bullet_width, bullet_height))
        self.rect = self.image.get_rect()
        self.rect.center = (x + (rect_width // 2), y + (rect_height // 2))
        self.speed_x = 5
        self.lado = lado

    def update(self):
        if self.lado:
            self.rect.x += self.speed_x
        elif self.lado == False:
            self.rect.x += -self.speed_x


"""class Proyectil(pygame.sprite.Sprite):
    def __init__(self, x, y,rect_width,rect_height,bullet_width,bullet_height,lado="rigth"):
        self.bullet_image = pygame.image.load('C:/Users/PC/OneDrive/Documents/GitHub/Python-segundo-cuatrimestre/TEMAS SEGUNDO PARCIAL/Practica py game/pygame_juego_figuras.py/Power/gema_roja.png').convert_alpha()
        self.bullet_width = bullet_width
        self.bullet_height = bullet_height
        self.image = pygame.transform.scale(self.bullet_image, (self.bullet_width, self.bullet_height))
        self.rect_width = rect_width
        self.rect_height = rect_height
        self.rect = self.image.get_rect()
        self.rect.center = (x+(rect_width//2), y+(rect_height//2))
        self.speed_x = 5
        self.lado = lado

    def do_shoot(self):
        if self.lado == "rigth":
            self.rect.x += self.speed_x
        elif self.lado == "left":
            self.rect.x += -self.speed_x     

    def update(self):
        self.do_shoot()"""
