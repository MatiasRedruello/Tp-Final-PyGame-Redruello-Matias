import pygame
from pygame.sprite import AbstractGroup
from clase_archivo import Archivo
from clase_proyectil import Proyectil
from clase_auxiliar import Suport


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
                lado,
                screen_width,
                screen_height) -> None:
        super().__init__()
        # Caracteristicas
        self.rect_speed_x = rect_speed_x # set
        self.rect_speed_y = rect_speed_y # set
        self.rect_width = rect_width
        self.rect_height = rect_height
        self.inicial_x = inicial_x #Donde Inicia en x
        self.inicial_y = inicial_y #Donde Inicia en y
        self.rect = pygame.Rect(self.inicial_x, self.inicial_y, self.rect_width, self.rect_height)   
        self.screen_width = screen_width   
        self.screen_height = screen_height
        self.lado = lado
        self.disparo_flag_random = True
        self.jump_height = 15
        self.gravity = 1
        self.jumping = False
        self.pixel_limit_rigth = pixel_limit_rigth #set
        self.pixel_limit_left = pixel_limit_left #set
        self.pixel_limit_y = pixel_limit_y
        self.sprites = pygame.sprite.Group()
        self.ultimo_disparo = 0
        self.timepo_control = Suport.propiedad_aleatoria()


    def gravity_settings(self):
        self.rect.y +=self.gravity #aplico gravedad
        # Controlar el salto
        if self.rect.y >= self.screen_height - self.pixel_limit_y: #pregunto donde esta el enemigo
            self.rect.y = self.screen_height - self.pixel_limit_y  #ubico al enemigo en eje y
        
    def do_walk(self):
        # Movimiento horizontal
        if self.lado == "True":
            self.rect.x += self.rect_speed_x
            # Limitar el movimiento a la derecha
            if self.rect.right > 800 - self.pixel_limit_rigth:# el valor maximo de panalla - los pixeles donde es ellimite
                self.rect.right = 800 - self.pixel_limit_rigth# lo tenes que ubicar en el mismo lugar que el cuadrado apra que no desaparece
                self.lado = "False"  # Cambia la dirección
        elif self.lado == "False":
            self.rect.x -= self.rect_speed_x
            # Limitar el movimiento a la izquierda
            if self.rect.left < 0 + self.pixel_limit_left: # el valor maximo de panalla - los pixeles donde es ellimite
                self.rect.left = 0 + self.pixel_limit_left # lo tenes que ubicar en el mismo lugar que el cuadrado apra que no desaparece
                self.lado = "True"  # Cambia la dirección    

    def do_shoot(self,tiempo_actual):
        
        if tiempo_actual-self.ultimo_disparo > self.timepo_control and self.disparo_flag_random:
            nuevo_proyectil_enemigo = Proyectil(self.rect.x,self.rect.y,
                                            self.rect.width,self.rect.height,"Power/gema_roja.png",
                                            10,10,
                                            10,True)
            self.sprites.add(nuevo_proyectil_enemigo)
            self.ultimo_disparo = tiempo_actual
            self.disparo_flag_random = False
        elif tiempo_actual-self.ultimo_disparo > self.timepo_control and not self.disparo_flag_random:
            nuevo_proyectil_enemigo = Proyectil(self.rect.x,self.rect.y,
                                            self.rect.width,self.rect.height,"Power/gema_roja.png",
                                            10,10,
                                            10,False)
            self.sprites.add(nuevo_proyectil_enemigo)
            self.ultimo_disparo = tiempo_actual 
            self.disparo_flag_random = True       
    
    def do_movement(self,tiempo):
        self.do_walk()
        self.gravity_settings()
        self.do_shoot(tiempo)
        
    def update(self):
         pass
          





