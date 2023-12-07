import pygame
from debug import DEBUG


class Item(pygame.sprite.Sprite):
    def __init__(self,inicial_x,
                inicial_y,item_path,lives_remaining=0) -> None:
        super().__init__()
        # Caracteristicas
        self.inicial_x = inicial_x 
        self.inicial_y = inicial_y
        self.item_image = pygame.image.load(item_path)        
        self.image = self.item_image # Heredo de sprite
        self.rect = self.item_image.get_rect()
        
        self.rect.topleft = (self.inicial_x, self.inicial_y)
            
        #cuando tenga el sprite va a servir 
        self.lives_remaining = lives_remaining 
        self.collide = False # Cantidad de vidas asociadas al corazón

        if self.lives_remaining > 0:
            self.counter = self.lives_remaining # Contador para las vidas restantes
            self.font = pygame.font.Font(None, 15)  # Fuente para el contador
        self.collected = False  # Bandera para saber si el ítem ha sido recogido


    def draw(self, screen):
        
            screen.blit(self.image, (self.rect.x -5, self.rect.y + 35)) # funde la imagen de las vidas
            # Dibuja el contador sobre el corazón si tiene vidas restantes
            text = self.font.render(str(self.counter), True, (255, 255, 255))
            screen.blit(text, (self.rect.centerx, self.rect.centery+40))  # Posición del contador de vidas

    def update(self):
        # Lógica de actualización si es necesario para el item
       if self.collected:
            self.kill()        





