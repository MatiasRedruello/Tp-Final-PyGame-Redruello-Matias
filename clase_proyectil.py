import pygame


bullet_image = pygame.image.load('Power/player_laser.png')#si json
bullet_width = 50#si json
bullet_height = 15#si json


class Proyectil(pygame.sprite.Sprite):
    def __init__(self, x, y,rect_width,rect_height, lado= True):
        super().__init__()
        self.player_x = x # Posicion del jugador en x necesario para disparar desde el jugador, class jugador
        self.player_y = y # Posicion del jugador en x necesario para disparar desde el jugador, class jugador
        self.rect_width = rect_width # Necesario para que el disparo salga del medio, class jugador
        self.rect_height =  rect_height # Necesario para que el disparo salga del medio, class jugador
        self.image = pygame.transform.scale(bullet_image, (bullet_width, bullet_height))#set
        self.rect = self.image.get_rect()
        self.rect.center = (self.player_x + (self.rect_width // 2), self.player_y + (self.rect_height // 2)) #tiene un porque,viene de la class jugador
        self.speed_x = 10 #set
        self.lado = lado # viene de main
    
    def do_shoot(self):
        if self.lado:
            self.rect.x += self.speed_x
        elif self.lado == False:
            self.rect.x += -self.speed_x
    def update(self):
        self.do_shoot()

