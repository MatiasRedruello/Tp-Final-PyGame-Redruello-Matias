import pygame

class PrimerMenu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.start_button = pygame.Rect(50, 100, 200, 50)  # Rectángulo para el botón "Start Game"
        self.exit_button = pygame.Rect(50, 200, 200, 50)   # Rectángulo para el botón "Exit"
        self.start_text = self.font.render("Start Game", True, (255, 255, 255))
        self.exit_text = self.font.render("Exit", True, (255, 255, 255))
        self.running = True

    def draw(self):
        pygame.draw.rect(self.screen, (0, 128, 255), self.start_button)
        pygame.draw.rect(self.screen, (0, 128, 255), self.exit_button)
        self.screen.blit(self.start_text, (self.start_button.x + 10, self.start_button.y + 10))
        self.screen.blit(self.exit_text, (self.exit_button.x + 10, self.exit_button.y + 10))

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.start_button.collidepoint(event.pos):
                    # Lógica para iniciar el juego
                    return "start_game"
                elif self.exit_button.collidepoint(event.pos):
                    self.running = False
        return None