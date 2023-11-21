import pygame


#si json
bullet_width = 50#si json
bullet_height = 15#si json


class Proyectil(pygame.sprite.Sprite):
    def __init__(self, x, y,rect_width,rect_height, bullet_path,
                    bullet_width ,
                    bullet_height ,
                    bullet_speed,lado= True,):
        super().__init__()
        self.bullet_path = bullet_path
        self.bullet_image = pygame.image.load(bullet_path)
        self.player_x = x # Posicion del jugador en x necesario para disparar desde el jugador, class jugador
        self.player_y = y # Posicion del jugador en x necesario para disparar desde el jugador, class jugador
        self.rect_width = rect_width # Necesario para que el disparo salga del medio, class jugador
        self.rect_height =  rect_height
        self.bullet_width = bullet_width
        self.bullet_height = bullet_height# Necesario para que el disparo salga del medio, class jugador
        self.image = pygame.transform.scale(self.bullet_image, (self.bullet_width, self.bullet_height))#set
        self.rect = self.image.get_rect()
        self.rect.center = (self.player_x + (self.rect_width // 2), self.player_y + (self.rect_height // 2)) #tiene un porque,viene de la class jugador
        self.bullet_speed = bullet_speed #set
        self.lado = lado # viene de main
    
    def do_shoot(self):
        if self.lado:
            self.rect.x += self.bullet_speed
        elif self.lado == False:
            self.rect.x += -self.bullet_speed
    def update(self):
        self.do_shoot()

