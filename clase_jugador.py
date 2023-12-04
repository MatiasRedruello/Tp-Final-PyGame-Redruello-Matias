import pygame
from debug import DEBUG
from clase_archivo import File
from clase_proyectil import Bullet
from clase_auxiliar import Suport
from clase_items import Item
class Player(pygame.sprite.Sprite):
    def __init__(self,screen_width,screen_height,plataform_list) -> None:
        super().__init__()
        # Caracteristicas
        
        self.archivo_json = File.json_load("info.json","r","level_one")
        self.rect_color = self.archivo_json.get("player").get("rect_color")
        self.rect_speed_x = self.archivo_json.get("player").get("rect_speed_x") # set
        self.rect_speed_y = self.archivo_json.get("player").get("rect_speed_y") # set
        self.rect_width = self.archivo_json.get("player").get("rect_width") 
        self.rect_height = self.archivo_json.get("player").get("rect_height")
        self.inicial_x = self.archivo_json.get("player").get("inicial_x") #Donde Inicia en x
        self.inicial_y = self.archivo_json.get("player").get("inicial_y") #Donde Inicia en y
        self.lives_remaining = self.archivo_json.get("player").get("lives_remaining")
        self.lives_path = self.archivo_json.get("player").get("lives_path")
        self.iddle_r = Suport.getSurfaceFromSpriteSheet("Player/Idle/player_idle.png", 5, 1, flip=False,step=1,scale=1)
        self.iddle_l = Suport.getSurfaceFromSpriteSheet("Player/Idle/player_idle.png", 5, 1, flip=True,step=1,scale=1)
        self.walk_r = Suport.getSurfaceFromSpriteSheet("Player/Walk/player_walk.png", 6, 1, flip=False,step=1,scale=1)
        self.walk_l = Suport.getSurfaceFromSpriteSheet("Player/Walk/player_walk.png", 6, 1, flip=True,step=1,scale=1)
        self.jump_r = Suport.getSurfaceFromSpriteSheet("Player/Jump/player_jump.png", 6, 1, flip=False,step=1,scale=1)
        self.jump_l = Suport.getSurfaceFromSpriteSheet("Player/Jump/player_jump.png", 6, 1, flip=True,step=1,scale=1)        
        self.frame_rate =120
        self.player_animation_time = 0
        self.player_move_time = 0


        self.initial_frame = 0 # Cuadro incial en cero (el primero)
        self.player_image_looking_rigth = True


        self.actual_animation = self.iddle_r # Es la lista de animacion con la que el personaje arranca
        self.actual_img_animation = self.actual_animation[self.initial_frame]# Primera imagen   
        self.image = self.actual_img_animation
        self.rect = self.image.get_rect() # Heredo de la clase sprite
        self.rect.topleft = (self.inicial_x, self.inicial_y)
        # pleyer collide 
        self.collide = False
        self.feet_size_width = 25 
        self.feet_size_height = 10 
        self.side_height = 55
        

        self.bullets_group = pygame.sprite.Group() 
        self.proyectil = self.archivo_json.get("player").get("proyectil")  
        self.jump_height = 18
        self.gravity = 1
        self.jumping = False
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.ultimo_disparo = 0
        self.timepo_control = 500  
        self.plataform_list = plataform_list
        self.score = 0
        self.define_collision_rects()
        self.lives = self.create_life_point()
        self.alive = True
    def jump_settings(self):
        self.rect_speed_y += self.gravity
        self.rect.y += self.rect_speed_y
        # Controlar el salto
        if self.rect.y > self.screen_height - self.rect.height:
            self.rect.y = self.screen_height - self.rect.height 
            self.jumping = False # reinicio el salto, si no slata una sola vez

    def stay(self):
        """
        self: Por defecto
        Descripcion:
        Permite que el personaje este quieto si no hay ninguna otra animacion distinta a iddle activa
        """          
        if self.actual_animation != self.iddle_l and self.actual_animation != self.iddle_r and not self.jumping:#no es ninguna de las otras y es iddle l o r
            self.actual_animation = self.iddle_r if self.player_image_looking_rigth else self.iddle_l
            self.initial_frame = 0

  
  
    def do_walk(self, letras_precionadas):
        if letras_precionadas[pygame.K_RIGHT] and not letras_precionadas[pygame.K_LEFT]:
            self.rect.x += self.rect_speed_x
            # Cambiar la velocidad horizontal solo si no está saltando
            if not self.jumping:
                self.actual_animation = self.walk_r
                self.player_image_looking_rigth = True  
            if self.rect.x > self.screen_width-self.rect.width:
                self.rect.x += -self.rect_speed_x
                self.actual_animation = self.iddle_r
                self.stay()
            # Resto del código de límites de movimiento derecho...
        elif letras_precionadas[pygame.K_LEFT] and not letras_precionadas[pygame.K_RIGHT]:
            self.rect.x += -self.rect_speed_x
            # Cambiar la velocidad horizontal solo si no está saltando
            if not self.jumping:
                self.actual_animation = self.walk_l
                self.player_image_looking_rigth = False 
            if self.rect.x < 0:
                self.rect.x += self.rect_speed_x
                self.actual_animation = self.iddle_l
                self.stay()                  
            # Resto del código de límites de movimiento izquierdo...
        elif not letras_precionadas[pygame.K_LEFT] or not letras_precionadas[pygame.K_RIGHT]:
            # Restablecer a la animación de quieto si no está saltando
            if not self.jumping:
                self.stay() 
        

    def do_jump(self,lista_de_eventos):
        # Detecta la tecla de espacio para activar el salto
        for event in lista_de_eventos:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not self.jumping and self.player_image_looking_rigth:
                self.jumping = True # me evita el salto multiple
                self.rect_speed_y = - self.jump_height 
                self.actual_animation = self.jump_r
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not self.jumping :
                self.jumping = True # me evita el salto multiple
                self.rect_speed_y = - self.jump_height 
                self.actual_animation = self.jump_l
               
        self.jump_settings()

    def do_shoot(self,lista_de_eventos,tiempo_actual,delta_ms):
        for event in lista_de_eventos:   
            if tiempo_actual-self.ultimo_disparo > self.timepo_control:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_d and not event.key == pygame.K_a and  self.player_image_looking_rigth:
                    nuevo_proyectil = Bullet(self.rect.x,self.rect.y,
                                                self.rect.width,self.rect.height,self.proyectil.get("bullet_path"),
                                                self.proyectil.get("bullet_scale"),
                                                self.proyectil.get("bullet_speed"),60,delta_ms,True)
                    self.bullets_group.add(nuevo_proyectil)
                    self.ultimo_disparo = tiempo_actual

            if tiempo_actual-self.ultimo_disparo > self.timepo_control:        
                # Detecta si se preciono la tecla de disparo a la izquierda  
                if event.type == pygame.KEYDOWN and event.key == pygame.K_a and not event.key == pygame.K_d and not self.player_image_looking_rigth:
                    nuevo_proyectil = Bullet(self.rect.x,self.rect.y,
                                                self.rect.width,self.rect.height,self.proyectil.get("bullet_path"),
                                                self.proyectil.get("bullet_scale"),
                                                self.proyectil.get("bullet_speed"),60,delta_ms,False)
                    nuevo_proyectil.delta_ms = delta_ms
                    self.bullets_group.add(nuevo_proyectil)          
                    self.ultimo_disparo = tiempo_actual

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

    def create_life_point(self):
        lives = Item(self.rect.x,self.rect.y,self.lives_path,self.lives_remaining)
        return lives

    def move_item_with_player(self):
        self.lives.rect.centerx = self.rect.centerx 
        self.lives.rect.bottom = self.rect.top - 10     

    def define_collision_rects(self):
        # Define las áreas rectangulares
        self.feet_rect = pygame.Rect(self.rect.centerx - self.feet_size_width // 2, self.rect.bottom - self.feet_size_height, self.feet_size_width, self.feet_size_height)
        self.head_rect = pygame.Rect(self.rect.centerx - self.feet_size_width // 2, self.rect.top - self.feet_size_height, self.feet_size_width, self.feet_size_height)
        self.left_rect = pygame.Rect(self.rect.left - 0, self.rect.top, self.feet_size_height, self.rect.height)
        self.right_rect = pygame.Rect(self.rect.right - self.feet_size_height, self.rect.top, self.feet_size_height, self.rect.height)  

    def do_movement(self,letras_precionadas,lista_de_eventos,tiempo_actual,delta_ms):
        self.do_walk(letras_precionadas)
        self.do_jump(lista_de_eventos)
        self.do_shoot(lista_de_eventos,tiempo_actual,delta_ms)
        self.do_animation(delta_ms)

    def update(self):
        self.define_collision_rects()
        self.move_item_with_player()
        
        #para actualizar la pósicion de la vida del jugador
 

    def draw(self,screen:pygame.surface.Surface):
        if self.alive:
            if DEBUG:
                pygame.draw.rect(screen,(255, 0, 0),self.rect,2)
                pygame.draw.rect(screen, (0,255,0), self.feet_rect,2)
                pygame.draw.rect(screen, (0,255,0), self.head_rect,2)
                pygame.draw.rect(screen, (255,255,0), self.right_rect,2)
                pygame.draw.rect(screen, (0,255,255), self.left_rect,2)
            self.image = self.actual_img_animation
            self.lives.draw(screen)
            screen.blit(self.image,self.rect)
        
          





