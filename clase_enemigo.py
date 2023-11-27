import pygame
from clase_proyectil import Bullet
from clase_auxiliar import Suport


"""x = 0
y = screen_height - rect_height"""
class Enemy(pygame.sprite.Sprite):
    def __init__(self,rect_speed_x,rect_speed_y,
                inicial_x  , 
                inicial_y  ,
                pixel_limit_rigth,
                pixel_limit_left,
                pixel_limit_y,
                bullet_path,
                walk_path,
                row,
                colum) -> None:
        super().__init__()
        # Caracteristicas
        self.rect_speed_x = rect_speed_x # set
        self.rect_speed_y = rect_speed_y # set
        self.initial_x = inicial_x #Donde Inicia en x
        self.initial_y = inicial_y #Donde Inicia en y
        self.bullet_path = bullet_path
        self.walk_path = walk_path

        self.walk_r = Suport.get_surface_from_spritesheet(self.walk_path, row, colum, flip=True)
        self.walk_l = Suport.get_surface_from_spritesheet(self.walk_path, row, colum)
     
        self.frame_rate =120
        self.player_animation_time = 0
        self.player_move_time = 0

        self.initial_frame = 0 # Cuadro incial en cero (el primero)
        self.actual_animation = self.walk_r # Es la lista de animacion con la que el personaje arranca
        self.actual_img_animation = self.actual_animation[self.initial_frame]# Primera imagen   
        self.image = self.actual_img_animation
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.initial_x, self.initial_y)

        self.enemy_image_looking_rigth = True
        self.disparo_flag_random = True
        self.jump_height = 15
        self.gravity = 1
        self.pixel_limit_rigth = pixel_limit_rigth #set
        self.pixel_limit_left = pixel_limit_left #set
        self.pixel_limit_y = pixel_limit_y # Lo tengo por la gravedad, tendria que sacar la gravedad de enemigo  y sacar esto
        self.bullets_group = pygame.sprite.Group()
        self.last_shot = 0
        self.time_control = Suport.random_shooting_time()


     #ubico al enemigo en eje y
        
    def do_walk(self):
        # Movimiento horizontal
        if  self.enemy_image_looking_rigth:
            self.rect.x += self.rect_speed_x
            self.actual_animation = self.walk_r
            # Limitar el movimiento a la derecha
            if self.rect.right > 800 - self.pixel_limit_rigth:# el valor maximo de panalla - los pixeles donde es ellimite
                self.rect.right = 800 - self.pixel_limit_rigth# lo tenes que ubicar en el mismo lugar que el cuadrado apra que no desaparece
                self.enemy_image_looking_rigth = False # Cambia la dirección
                self.actual_animation = self.walk_l
        elif not self.enemy_image_looking_rigth:
            self.rect.x -= self.rect_speed_x
            self.actual_animation = self.walk_l 
            # Limitar el movimiento a la izquierda
            if self.rect.left < 0 + self.pixel_limit_left: # el valor maximo de panalla - los pixeles donde es ellimite
                self.rect.left = 0 + self.pixel_limit_left # lo tenes que ubicar en el mismo lugar que el cuadrado apra que no desaparece
                self.enemy_image_looking_rigth = True  # Cambia la dirección    
                self.actual_animation = self.walk_r 

    def do_shoot(self,initial_time):
        if initial_time-self.last_shot > self.time_control and self.disparo_flag_random and self.enemy_image_looking_rigth:
            new_enemy_bullet = Bullet(self.rect.x,self.rect.y,
                                            self.rect.width,self.rect.height,self.bullet_path,
                                            (10,10),
                                            6,True)
            self.bullets_group.add(new_enemy_bullet)
            self.last_shot = initial_time
            self.disparo_flag_random = False
        elif initial_time-self.last_shot > self.time_control and not self.disparo_flag_random and not self.enemy_image_looking_rigth:
            new_enemy_bullet = Bullet(self.rect.x,self.rect.y,
                                            self.rect.width,self.rect.height,self.bullet_path,
                                            (10,10),
                                            6,False)
            self.bullets_group.add(new_enemy_bullet)
            self.last_shot = initial_time 
            self.disparo_flag_random = True       
    def do_animation(self,delta_ms):
        """
        self: Por defecto
        delta_ms: Permite controla la ejecucion de una aniacion 
        Descripcion:
        Controla el teimpo de animacion y ademas permite que se pase de una imagen a la siguiente
        """        
            # en initial frame se guarda un numero del indice de la imagen que queremos mostrar
        self.player_animation_time += delta_ms 
        if self.player_animation_time >= self.frame_rate:
            self.player_animation_time = 0
            # en initial frame se guarda un numero del indice de la imagen que queremos mostrar
            if self.initial_frame < len(self.actual_animation) - 1: # mientras ese indice es menor al ultimo indice de la imagen sumo uno
                self.initial_frame += 1
            else:
                self.initial_frame = 0
                
            self.actual_img_animation = self.actual_animation[self.initial_frame]
            self.image = self.actual_img_animation

    def do_movement(self,time,delta_ms):
        self.do_walk()
        self.do_shoot(time)
        self.do_animation(delta_ms)
    def update(self):
         pass
          





