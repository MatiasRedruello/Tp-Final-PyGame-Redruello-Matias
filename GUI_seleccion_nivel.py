import pygame

class SeleccionNivel:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.level_one_button = pygame.Rect(50, 100, 200, 50)
        self.level_two_button = pygame.Rect(50, 200, 200, 50)
        self.level_three_button = pygame.Rect(50, 300, 200, 50)
        self.level_one_text = self.font.render("Level One", True, (255, 255, 255))
        self.level_two_text = self.font.render("Level Two", True, (255, 255, 255))
        self.level_three_text = self.font.render("Level Three", True, (255, 255, 255))
        self.running = True
        self.selected_level = None
        self.force_level = False

    def draw(self):
        pygame.draw.rect(self.screen, (0, 128, 255), self.level_one_button)
        pygame.draw.rect(self.screen, (0, 128, 255), self.level_two_button)
        pygame.draw.rect(self.screen, (0, 128, 255), self.level_three_button)
        self.screen.blit(self.level_one_text, (self.level_one_button.x + 10, self.level_one_button.y + 10))
        self.screen.blit(self.level_two_text, (self.level_two_button.x + 10, self.level_two_button.y + 10))
        self.screen.blit(self.level_three_text, (self.level_three_button.x + 10, self.level_three_button.y + 10))

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.level_one_button.collidepoint(event.pos):
                    self.selected_level = "level_one"
                elif self.level_two_button.collidepoint(event.pos):
                    self.selected_level = "level_two"
                elif self.level_three_button.collidepoint(event.pos):
                    self.selected_level = "level_three"
        return self.selected_level
