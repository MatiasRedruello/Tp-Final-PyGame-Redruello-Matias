import pygame



class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, rect_width, rect_height, bullet_path,bullet_scale,
                bullet_speed,frame_rate,delta_ms,lado=True):
        super().__init__()
        self.bullet_path = bullet_path
        self.bullet_image = pygame.image.load(bullet_path)
        self.player_x = x
        self.player_y = y
        self.rect_width = rect_width
        self.rect_height = rect_height
        self.image = pygame.transform.scale(self.bullet_image,bullet_scale)
        self.rect = self.image.get_rect()
        self.frame_rate = frame_rate
        self.bullet_animation_time = 0
        self.delta_ms = delta_ms
        # Definir posición basada en el lado del jugador
        if lado:  # Si está mirando a la derecha
            self.rect.left = self.player_x + self.rect_width  # Disparo desde el lado derecho

        else:  # Si está mirando a la izquierda
            self.rect.right = self.player_x  # Disparo desde el lado izquierdo
            
        self.rect.centery = self.player_y + (self.rect_height // 2)
        self.bullet_speed = bullet_speed
        self.lado = lado

    def do_shoot(self):
        self.bullet_animation_time += self.delta_ms 
        if self.bullet_animation_time >= self.frame_rate:
            self.bullet_animation_time = 0        
            if self.lado:
                self.rect.x += self.bullet_speed
            else:
                self.rect.x -= self.bullet_speed


    def draw(self,screen:pygame.surface.Surface):
        pass
        
    def update(self):
        self.do_shoot()
        
