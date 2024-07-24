import pygame
from clase_proyectil import Bullet
from clase_auxiliar import Suport
from clase_items import Item
from debug import DEBUG
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
                colum,
                separate_files,
                lives_remaining,
                lives_path,attack_path,die_path,sound_enemy_damege) -> None:
        super().__init__()
        # Caracteristicas
        self.rect_speed_x = rect_speed_x # set
        self.rect_speed_y = rect_speed_y # set
        self.initial_x = inicial_x #Donde Inicia en x
        self.initial_y = inicial_y #Donde Inicia en y
        self.separate_files = separate_files
        if self.separate_files == "no":
            self.bullet_path = bullet_path
            self.walk_r = Suport.getSurfaceFromSpriteSheet(walk_path, colum, row, flip=True,step=1,scale=0.5)
            self.walk_l = Suport.getSurfaceFromSpriteSheet(walk_path, colum, row, flip=False,step=1,scale=0.5)
        elif self.separate_files =="yes":
            self.walk_r = Suport.getSurfaceFromSeparateFiles(walk_path,0,10,flip=False,scale=0.1)
            self.walk_l = Suport.getSurfaceFromSeparateFiles(walk_path,0,10,flip=True,scale=0.1)
            self.mele_attack_r = Suport.getSurfaceFromSeparateFiles(attack_path,0,10,flip=False,scale=0.1)
            self.mele_attack_l = Suport.getSurfaceFromSeparateFiles(attack_path,0,10,flip=True,scale=0.1)
            self.die_r = Suport.getSurfaceFromSeparateFiles(die_path,0,10,flip=False,scale=0.1)
            self.die_l = Suport.getSurfaceFromSeparateFiles(die_path,0,10,flip=True,scale=0.1)
        self.lives_remaining = lives_remaining
        self.lives_path = lives_path
        self.frame_rate =120
        self.enemy_animation_time = 0
        self.enemy_move_time = 0

        self.initial_frame = 0 # Cuadro incial en cero (el primero)
        self.actual_animation = self.walk_r # Es la lista de animacion con la que el personaje arranca
        self.actual_img_animation = self.actual_animation[self.initial_frame]# Primera imagen   
        self.image = self.actual_img_animation
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.initial_x, self.initial_y)

        #nemy colllide
        self.feet_size_width = 25 
        self.feet_size_height = 10 
        self.side_height = 50
        self.define_collision_rects()  
              
        self.enemy_image_looking_rigth = True
        self.disparo_flag_random = True
        self.jump_height = 15
        self.gravity = 1
        self.pixel_limit_rigth = pixel_limit_rigth #set
        self.pixel_limit_left = pixel_limit_left #set
        self.pixel_limit_y = pixel_limit_y # Lo tengo por la gravedad, tendria que sacar la gravedad de enemigo  y sacar esto
        self.bullets_group = pygame.sprite.Group()

        self.lives = self.create_life_point()
        self.last_shot = 0
        self.time_control = Suport.random_shooting_time()
        self.alive = True #controla que el enemigo este vivo
        self.mele_attack = False #controla ataque  mele
        #sonidos
        self.sound_damege = pygame.mixer.Sound(sound_enemy_damege)
     #ubico al enemigo en eje y
        
    def do_walk(self):
        # Movimiento horizontal
             
            if  self.enemy_image_looking_rigth:
                self.rect.x += self.rect_speed_x
                self.actual_animation = self.walk_r
                
                # Limitar el movimiento a la derecha
                if self.rect.right > 1000 - self.pixel_limit_rigth:# el valor maximo de panalla - los pixeles donde es ellimite
                    self.rect.right = 1000 - self.pixel_limit_rigth# lo tenes que ubicar en el mismo lugar que el cuadrado apra que no desaparece
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



            

   
    def do_shoot(self,initial_time,delta_ms):
        
        if initial_time-self.last_shot > self.time_control and self.disparo_flag_random and self.enemy_image_looking_rigth and self.separate_files == "no":
            new_enemy_bullet = Bullet(self.rect.x,self.rect.y,
                                            self.rect.width,self.rect.height,self.bullet_path,
                                            (30,30),
                                            10,30,delta_ms,True)
            
            self.bullets_group.add(new_enemy_bullet)
            self.last_shot = initial_time
            self.disparo_flag_random = False
        elif initial_time-self.last_shot > self.time_control and not self.disparo_flag_random and not self.enemy_image_looking_rigth and self.separate_files == "no":
            new_enemy_bullet = Bullet(self.rect.x,self.rect.y,
                                            self.rect.width,self.rect.height,self.bullet_path,
                                            (30,30),
                                            10,30,delta_ms,False)

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
        self.enemy_animation_time += delta_ms 
        if self.enemy_animation_time >= self.frame_rate:
            self.enemy_animation_time = 0
            # en initial frame se guarda un numero del indice de la imagen que queremos mostrar
            if self.initial_frame < len(self.actual_animation) - 1: # mientras ese indice es menor al ultimo indice de la imagen sumo uno
                self.initial_frame += 1
            else:
                self.initial_frame = 0
                
            self.actual_img_animation = self.actual_animation[self.initial_frame]
            self.image = self.actual_img_animation

    def define_collision_rects(self):
        # Define las áreas rectangulares
        self.feet_rect = pygame.Rect(self.rect.centerx - self.feet_size_width // 2, self.rect.bottom - self.feet_size_height, self.feet_size_width, self.feet_size_height)
        self.head_rect = pygame.Rect(self.rect.centerx - self.feet_size_width // 2, self.rect.top - self.feet_size_height, self.feet_size_width, self.feet_size_height)
        self.left_rect = pygame.Rect(self.rect.left +25, self.rect.top+30, self.feet_size_height , self.rect.height//2)
        self.right_rect = pygame.Rect(self.rect.right-25, self.rect.top+30, self.feet_size_height, self.rect.height//2)  
    
    
        # Acciones adicionales antes de eliminar al enemigo, si las hay
    def kill(self):
        if self.lives_remaining == 0:
            self.bullets_group.empty()
            self.lives.kill()
            self.alive = False  # Establecer la bandera 'alive' en False cuando el enemigo muere
            super().kill()
    
            

    def do_movement(self,time,delta_ms):
  
        self.do_walk()
        self.do_shoot(time,delta_ms)
        self.do_animation(delta_ms)
        
    def create_life_point(self):
        lives = Item(self.rect.x,self.rect.y,self.lives_path,self.lives_remaining)
        return lives

    def move_item_with_enemy(self):
        self.lives.rect.centerx = self.rect.centerx 
        self.lives.rect.bottom = self.rect.top - 10 
    
    def update(self):
       
        self.define_collision_rects()
        self.move_item_with_enemy()
        self.kill()
        #para actualizar la vida del enemigo

        
    def draw(self,screen:pygame.surface.Surface):
        # Cuando esta vivo se dibuja
        if self.alive:
            if DEBUG:
                pygame.draw.rect(screen,(255, 0, 0),self.rect,2)
                pygame.draw.rect(screen, (0,255,0), self.feet_rect,2)
                pygame.draw.rect(screen, (0,255,0), self.head_rect,2)
                pygame.draw.rect(screen, (255,255,0), self.right_rect,2)
                pygame.draw.rect(screen, (0,255,255), self.left_rect,2)
            self.lives.draw(screen)
            screen.blit(self.image,self.rect)    
            
        





