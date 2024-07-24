import pygame

class PrimerMenu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.background_image = pygame.image.load('background/layer_08_1920 x 1080.png').convert()
        self.background_image = pygame.transform.scale(self.background_image, (self.screen.get_width(), self.screen.get_height()))
        self.start_button = pygame.Rect(400, 100, 200, 50)  # Rectángulo para el botón "Start Game"
        self.exit_button = pygame.Rect(400, 200, 200, 50)   # Rectángulo para el botón "Exit"
        self.start_text = self.font.render("Start Game", True, (255, 255, 255))
        self.exit_text = self.font.render("Exit", True, (255, 255, 255))
        self.running = True

    def draw(self):
        self.screen.blit(self.background_image, (0, 0))
        pygame.draw.rect(self.screen, (170, 136, 85), self.start_button,3)
        pygame.draw.rect(self.screen, (170, 136, 85), self.exit_button,3)
        self.screen.blit(self.start_text, (self.start_button.x + 10, self.start_button.y + 10))
        self.screen.blit(self.exit_text, (self.exit_button.x + 10, self.exit_button.y + 10))

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.start_button.collidepoint(event.pos):
                    # Lógica para iniciar el juego
                    return "start_game"
                elif self.exit_button.collidepoint(event.pos):
                    return "exit"
        