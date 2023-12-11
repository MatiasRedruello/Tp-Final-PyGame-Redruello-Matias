import pygame

class BarraVolumen:
    def __init__(self, screen, x, y, width, height, color, initial_volume):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.volume = initial_volume
        self.x = (screen.get_width() - self.width) // 2
        self.y = 250

        self.font = pygame.font.SysFont("Arial", 18)
        self.text_color = (255, 255, 255)
        self.text_surface = None
        self.text_rect = None
        self.actualizar_texto_porcentaje()


    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
        # Dibuja la barra llena según el volumen actual
        pygame.draw.rect(self.screen, (255, 0, 0), (self.x, self.y, self.width * self.volume, self.height))
        if self.text_surface:
            self.screen.blit(self.text_surface, self.text_rect)

        
    def clic(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height:
                # Calcula el nuevo volumen basado en la posición del clic
                self.volume = (mouse_x - self.x) / self.width
                self.volume = max(0, min(1, self.volume))  # Asegurarse de que el volumen esté entre 0 y 1
                self.actualizar_texto_porcentaje()
        elif event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
            # Actualizar continuamente el volumen mientras se mantiene presionado el clic y se mueve el ratón
            mouse_x, _ = pygame.mouse.get_pos()
            self.volume = (mouse_x - self.x) / self.width
            self.volume = max(0, min(1, self.volume))  # Asegurarse de que el volumen esté entre 0 y 1
            self.actualizar_texto_porcentaje()
    def actualizar_texto_porcentaje(self):
        # Actualizar el texto del porcentaje
        porcentaje = f"{int(self.volume * 100)}%"
        self.text_surface = self.font.render(porcentaje, True, self.text_color)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = (self.x + self.width + self.text_rect.width // 2 + 10, self.y + self.height // 2)

    def update(self, nuevo_volumen):
        self.actualizar_texto_porcentaje()
        self.volume = nuevo_volumen
        self.actualizar_texto_porcentaje()
