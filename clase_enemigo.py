import pygame
from clase_proyectil import Bullet
from clase_auxiliar import suport


"""x = 0
y = screen_height - rect_height"""
class Enemy(pygame.sprite.Sprite):
    def __init__(self,rect_speed_x,rect_speed_y,
                rect_width,
                rect_height,
                inicial_x  , 
                inicial_y  ,
                pixel_limit_rigth,
                pixel_limit_left,
                pixel_limit_y,
                screen_width,
                screen_height) -> None:
        super().__init__()
        # Caracteristicas
        self.rect_speed_x = rect_speed_x # set
        self.rect_speed_y = rect_speed_y # set
        self.rect_width = rect_width
        self.rect_height = rect_height
        self.initial_x = inicial_x #Donde Inicia en x
        self.initial_y = inicial_y #Donde Inicia en y
        self.rect = pygame.Rect(self.initial_x, self.initial_y, self.rect_width, self.rect_height)   
        self.screen_width = screen_width   
        self.screen_height = screen_height
        self.side = True
        self.disparo_flag_random = True
        self.jump_height = 15
        self.gravity = 1
        self.pixel_limit_rigth = pixel_limit_rigth #set
        self.pixel_limit_left = pixel_limit_left #set
        self.pixel_limit_y = pixel_limit_y # Lo tengo por la gravedad, tendria que sacar la gravedad de enemigo  y sacar esto
        self.bullets_group = pygame.sprite.Group()
        self.last_shot = 0
        self.time_control = suport.random_shooting_time()


    def gravity_settings(self):
        self.rect.y +=self.gravity #aplico gravedad
        # Controlar el salto
        if self.rect.y >= self.screen_height - self.pixel_limit_y: #pregunto donde esta el enemigo
            self.rect.y = self.screen_height - self.pixel_limit_y  #ubico al enemigo en eje y
        
    def do_walk(self):
        # Movimiento horizontal
        if self.side == True:
            self.rect.x += self.rect_speed_x
            # Limitar el movimiento a la derecha
            if self.rect.right > 800 - self.pixel_limit_rigth:# el valor maximo de panalla - los pixeles donde es ellimite
                self.rect.right = 800 - self.pixel_limit_rigth# lo tenes que ubicar en el mismo lugar que el cuadrado apra que no desaparece
                self.side = False  # Cambia la dirección
        elif self.side == False:
            self.rect.x -= self.rect_speed_x
            # Limitar el movimiento a la izquierda
            if self.rect.left < 0 + self.pixel_limit_left: # el valor maximo de panalla - los pixeles donde es ellimite
                self.rect.left = 0 + self.pixel_limit_left # lo tenes que ubicar en el mismo lugar que el cuadrado apra que no desaparece
                self.side = True  # Cambia la dirección    

    def do_shoot(self,initial_time):
        if initial_time-self.last_shot > self.time_control and self.disparo_flag_random:
            new_enemy_bullet = Bullet(self.rect.x,self.rect.y,
                                            self.rect.width,self.rect.height,"Power/gema_roja.png",
                                            10,10,
                                            10,True)
            self.bullets_group.add(new_enemy_bullet)
            self.last_shot = initial_time
            self.disparo_flag_random = False
        elif initial_time-self.last_shot > self.time_control and not self.disparo_flag_random:
            new_enemy_bullet = Bullet(self.rect.x,self.rect.y,
                                            self.rect.width,self.rect.height,"Power/gema_roja.png",
                                            10,10,
                                            10,False)
            self.bullets_group.add(new_enemy_bullet)
            self.last_shot = initial_time 
            self.disparo_flag_random = True       
    
    def do_movement(self,time):
        self.do_walk()
        self.gravity_settings()
        self.do_shoot(time)
        
    def update(self):
         pass
          





