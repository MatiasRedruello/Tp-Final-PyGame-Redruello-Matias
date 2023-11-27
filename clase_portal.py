import pygame
from clase_archivo import File
from clase_auxiliar import Suport


"""x = 0
y = screen_height - rect_height"""
class Portal(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        # Caracteristicas
        self.inicial_x = 0 
        self.inicial_y = 0
        self.portal_path = r"Portal/teleporter_visible__x1_portal_png_1354836401.png"
        self.item_image = Suport.get_surface_from_spritesheet(self.portal_path,5,3)        

        self.frame_rate =200
        self.player_animation_time = 0
        self.player_move_time = 0

        self.initial_frame = 0 # Cuadro incial en cero (el primero)
        self.actual_animation = self.item_image # Es la lista de animacion con la que el personaje arranca
        self.actual_img_animation = self.actual_animation[self.initial_frame]# Primera imagen  
        #self.actual_img_animation = pygame.transform.scale(self.actual_img_animation,(10,10)) 
        self.image = pygame.transform.scale(self.actual_img_animation,(100,100))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.inicial_x, self.inicial_y)
    def scale_imaage(self):
        self.actual_img_animation = self.actual_animation[self.initial_frame]
        self.image = pygame.transform.scale(self.actual_img_animation,(150,150))

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
            self.scale_imaage()   
            

    def update(self):       
        pass



