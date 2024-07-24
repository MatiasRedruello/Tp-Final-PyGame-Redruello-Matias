import pygame
from utils import *
class TablaPuntajes():
    def __init__(self,screen_with,diccionario_puntajes) -> None:
        self.screen_with = screen_with
        self.diccionario_puntajes = diccionario_puntajes

        self.img_tabla_puntajes = pygame.image.load(r'Recursos puntaje/img/tabla_puntajes.png')
        self.pos_img_tabla_puntajes = ((self.screen_with - self.img_tabla_puntajes.get_width()) // 2, 120)

        # Creamos el texto del titulo
        self.font_titulo = pygame.font.Font(r'Recursos puntaje/fonts/Halimount.otf', 50)
        self.txt_titulo = self.font_titulo.render("Puntajes", True, "white")
        self.pos_txt_titulo = ((self.screen_with - self.txt_titulo.get_width()) // 2, 155)

        # Creamos el texto del boton
        self.font_boton = pygame.font.Font(r'Recursos puntaje/fonts/Halimount.otf', 30)
        self.txt_boton = self.font_boton.render("Jugar de nuevo", True, "white")
        self.pos_txt_boton = ((self.screen_with - self.txt_titulo.get_width()) // 2, 635)

        # Creamos el texto de la tabla
        self.font_tabla = pygame.font.Font(r'Recursos puntaje/fonts/Halimount.otf', 35)
        self.lista_puntaje_txt = []

        self.y = 245
    def table(self):
        
        for clave,valor in self.diccionario_puntajes.items():
            # Si estamos en la primera vuelta, utilizamos la tipografia color blanco
            if len(self.lista_puntaje_txt) == 0:
                color_txt = (255, 255, 255)
            else:
                color_txt = (109, 30, 3)

          
            nombre_txt = self.font_tabla.render(formatear_nombre_jugador(str(clave)), True, color_txt)
            puntaje_txt = self.font_tabla.render(formatear_puntaje(str(valor)), True, color_txt)

          
            self.lista_puntaje_txt.append((nombre_txt, (360, self.y)))
            self.lista_puntaje_txt.append((puntaje_txt, (520, self.y)))

            self.y += 50  
        
    def draw(self,screen):
        screen.blit(self.img_tabla_puntajes, self.pos_img_tabla_puntajes)
        screen.blit(self.txt_titulo, self.pos_txt_titulo)
        screen.blits(self.lista_puntaje_txt)
        screen.blit(self.txt_boton, self.pos_txt_boton) 
        
    def update(self):
        self.table()