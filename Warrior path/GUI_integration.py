import pygame
from GUI_menu_principal import PrimerMenu
from GUI_seleccion_nivel import SeleccionNivel

class GuiIntegration():
    def __init__(self,screen) -> None:
        self.screen = screen
        self.primer_menu = PrimerMenu(self.screen)
        self.level_selection  = SeleccionNivel(self.screen)
        self.running_game = False
    def menu(self):
        while self.primer_menu.running:
            clicked = self.primer_menu.check_events()
            self.screen.fill((0, 0, 0)) 
            self.primer_menu.draw()
            pygame.display.update()
            if clicked == "start_game":
                self.primer_menu.running = False
                self.level_selection.running = True
                            
            elif clicked == "exit":
                self.primer_menu.running = False 

            while self.level_selection.running:
                    load_level = self.level_selection.check_events()
                    if load_level == "level_one":
                        self.running_game = True
                        return  "level_one"
                    #controlo que si eligen nivel dos o tres tener lo requisitos necesario para que no rompa
                    elif load_level == "level_two": 
                        self.level_selection.force_level = True
                        self.running_game = True
                        return  "level_one"
                    elif  load_level == "level_three":
                        self.level_selection.force_level = True
                        self.running_game = True
                        return  "level_two"

                    self.screen.fill((0, 0, 0))
                    self.level_selection.draw()
                    pygame.display.update()       