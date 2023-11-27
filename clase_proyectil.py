import pygame



class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, rect_width, rect_height, bullet_path,
                 bullet_width, bullet_height, bullet_speed, lado=True):
        super().__init__()
        self.bullet_path = bullet_path
        self.bullet_image = pygame.image.load(bullet_path)
        self.player_x = x
        self.player_y = y
        self.rect_width = rect_width
        self.rect_height = rect_height
        self.image = self.bullet_image
        self.rect = self.image.get_rect()

        # Definir posición basada en el lado del jugador
        if lado:  # Si está mirando a la derecha
            self.rect.left = self.player_x + self.rect_width  # Disparo desde el lado derecho

        else:  # Si está mirando a la izquierda
            self.rect.right = self.player_x  # Disparo desde el lado izquierdo
            
        self.rect.centery = self.player_y + (self.rect_height // 2)
        self.bullet_speed = bullet_speed
        self.lado = lado

    def do_shoot(self):
        if self.lado:
            self.rect.x += self.bullet_speed
        else:
            self.rect.x -= self.bullet_speed

    def update(self):
        self.do_shoot()
