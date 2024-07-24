import pygame


class ControladorVolumen:
    def __init__(self, ruta_musica):
        self.ruta_musica = ruta_musica
        self.volumen = 0.5  # Volumen inicial al 50%
        pygame.mixer.init()
        self.musica = pygame.mixer.Sound(self.ruta_musica)
        self.musica.set_volume(self.volumen)
        self.musica.play(-1)
        

    def aumentar_volumen(self, incremento):
        self.volumen = min(1.0, self.volumen + incremento)
        self.musica.set_volume(self.volumen)

    def disminuir_volumen(self, decremento):
        self.volumen = max(0.0, self.volumen - decremento)
        self.musica.set_volume(self.volumen)

    def obtener_volumen_porcentual(self):
        return int(self.volumen * 100)
