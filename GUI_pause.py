import pygame



class BotonPausa:
    def __init__(self, screen,controlador_volumen):
        self.screen = screen
        self.width = 100
        self.height = 50

        self.font = pygame.font.SysFont("Arial", 24)

        self.pressed = False
        self.color_normal = (50, 50, 50)
        self.color_presionado = (100, 100, 100)
        self.color_texto = (255, 255, 255)
        self.color_borde = (255, 255, 255)
        self.barra_x = 400
        self.barra_y = 15
        self.barra_ancho = 200
        self.barra_alto = 50
        self.text_surface = self.font.render("Pausa", True, self.color_texto)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.topright = (screen.get_width() - 10, 10)
        
        self.pausa = False
        self.controlador_volumen = controlador_volumen  # Añadir el controlador de volumen
        


    def aumentar_volumen(self):
        self.controlador_volumen.aumentar_volumen(0.1)  # Puedes ajustar el incremento/decremento como desees

    def disminuir_volumen(self):
        self.controlador_volumen.disminuir_volumen(0.1)  # Puedes ajustar el incremento/decremento como desees

    def clic(self, event):
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.text_rect.collidepoint(event.pos):
                self.pressed = not self.pressed
                self.pausa = not self.pausa  # Alternar el estado de pausa
                if not self.pausa:  # Si se desactiva la pausa, resetea el botón de pausa
                    self.reset()
            elif self.pressed:
            # Verificar si el clic está dentro de la barra de volumen
                barra_rect = pygame.Rect(self.barra_x, self.barra_y, self.barra_ancho, self.barra_alto)
                if barra_rect.collidepoint(event.pos):
                    self.ajustar_volumen_con_barra(event.pos)
        
    def draw_volume_bar(self):
    # Solo dibujar la barra si el juego está en pausa
        if self.pressed:
            # Dibujar la barra de volumen
            barra_color = (173, 216, 230)
            barra_rect = pygame.Rect(self.barra_x, self.barra_y, self.barra_ancho, self.barra_alto)
            pygame.draw.rect(self.screen, barra_color, barra_rect)

            # Calcular el indicador del volumen actual
            volumen_actual_rect = pygame.Rect(barra_rect.left, barra_rect.top,
                                            barra_rect.width * self.controlador_volumen.volumen, barra_rect.height)
            volumen_actual_color = (255, 255, 153)  # Color del indicador
            pygame.draw.rect(self.screen, volumen_actual_color, volumen_actual_rect)

            porcentaje_text = f"{int(self.controlador_volumen.volumen * 100)}%"  # Obtener el porcentaje
   
            # Dibujar la palabra "Sound" sobre la barra
            font = pygame.font.Font(None, 24)
            sound_text = font.render("Sound", True, (255, 255, 255))  # Color blanco
            sound_rect = sound_text.get_rect()
            sound_rect.midright = (barra_rect.left + 60, barra_rect.centery)  # Alinear a la derecha de la barra
            self.screen.blit(sound_text, sound_rect)
            # Redimensionar el porcentaje al ancho de la barra y la mitad de la altura de la barra
            porcentaje_surface = font.render(porcentaje_text, True, (255, 255, 255))  # Color blanco
            porcentaje_surface = pygame.transform.scale(porcentaje_surface, (25, 25))
            porcentaje_rect = porcentaje_surface.get_rect()
            porcentaje_rect.midright = (sound_rect.right + 100, barra_rect.centery)  # Alinear a la izquierda de "Sound"
            self.screen.blit(porcentaje_surface, porcentaje_rect)

            # Rellenar el área del porcentaje con el color del fondo
            fondo_color = (173, 216, 230)  # Cambia este color según tu diseño de fondo
            self.screen.fill(fondo_color, porcentaje_rect)

            # Dibujar el nuevo porcentaje
            self.screen.blit(porcentaje_surface, porcentaje_rect)

    def ajustar_volumen_con_barra(self, pos_mouse):
        if self.pressed:  # Verifica que la pausa esté activa
            # Lógica para ajustar el volumen basado en la posición del mouse en la barra
            pos_rel = pos_mouse[0] - self.barra_x  # Calcular posición relativa respecto al inicio de la barra
            pos_rel = max(0, min(pos_rel, self.barra_ancho))  # Limitar la posición relativa al ancho de la barra
            nuevo_volumen = pos_rel / self.barra_ancho  # Calcular el nuevo volumen basado en la posición relativa

            # Ajustar el volumen usando los métodos de ControladorVolumen
            print(f"Posición relativa: {pos_rel}")  # Imprimir la posición relativa del mouse
            print(f"Nuevo volumen calculado: {nuevo_volumen}")  # Imprimir el nuevo volumen calculado

            # Si el nuevo volumen es diferente al actual, ajustamos el volumen
            if nuevo_volumen != self.controlador_volumen.volumen:
                self.controlador_volumen.volumen = nuevo_volumen
                self.controlador_volumen.musica.set_volume(nuevo_volumen)

    def reset(self):
        self.pressed = False

    def draw(self):
        if self.pressed:
            color_actual = self.color_presionado
            self.draw_volume_bar()
        else:
            color_actual = self.color_normal
        
        pygame.draw.rect(self.screen, color_actual, self.text_rect)
        pygame.draw.rect(self.screen, self.color_borde, self.text_rect, 2)
        self.screen.blit(self.text_surface, self.text_rect)

    def update(self):
        pass