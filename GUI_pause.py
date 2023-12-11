import pygame
from GUI_barra_volumen import BarraVolumen
pygame
from GUI_barra_volumen import BarraVolumen

class BotonPausa:
    def __init__(self, screen):
        self.screen = screen
        self.width = 100
        self.height = 50

        self.font = pygame.font.SysFont("Arial", 24)

        self.pressed = False
        self.color_normal = (50, 50, 50)
        self.color_presionado = (100, 100, 100)
        self.color_texto = (255, 255, 255)
        self.color_borde = (255, 255, 255)
        
        self.text_surface = self.font.render("Pausa", True, self.color_texto)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.topright = (screen.get_width() - 10, 10)
        
        self.pausa = False
        self.mostrar_barra_volumen = False
        self.barra_volumen = BarraVolumen(screen, 200, 200, 200, 20, (150, 150, 150), 0.5)

    def clic(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.text_rect.collidepoint(event.pos):
                self.pressed = not self.pressed
                self.pausa = not self.pausa  # Alternar el estado de pausa
        if self.pausa:
            self.barra_volumen.clic(event)
    def reset(self):
        self.pressed = False

    def draw(self):
        if self.pressed:
            color_actual = self.color_presionado
        else:
            color_actual = self.color_normal

        pygame.draw.rect(self.screen, color_actual, self.text_rect)
        pygame.draw.rect(self.screen, self.color_borde, self.text_rect, 2)
        self.screen.blit(self.text_surface, self.text_rect)
        if self.pausa:
            self.barra_volumen.draw()
    def update(self):
        pass