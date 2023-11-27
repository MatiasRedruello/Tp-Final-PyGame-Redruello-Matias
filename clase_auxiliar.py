import random
import pygame
class Suport():
    @staticmethod
    def random_shooting_time():
        # Generar un valor aleatorio (0 o 1)
        value = random.choice([500,])
        # Si el valor es 1, devuelve True; de lo contrario, devuelve False
        return value 
       
    @staticmethod # lo puedo usar sin instancial la clase
    def get_surface_from_spritesheet(img_path: str, cols: int, rows: int, step = 1, flip: bool = False) -> list[pygame.surface.Surface]:
        """
        Obtiene una lista de superficies a partir de una hoja de sprites.

        Parámetros:
        - img_path (str): Ruta de la imagen de la hoja de sprites.
        - cols (int): Cantidad de columnas en la hoja de sprites.
        - rows (int): Cantidad de filas en la hoja de sprites.
        - step (int, opcional): Valor que determina cómo recorrer la hoja de sprites (por defecto, 1).
        - flip (bool, opcional): Indica si se debe voltear horizontalmente la imagen (por defecto, False).

        Retorna:
        Una lista de superficies, cada una representando un sprite individual.

        Descripción:
        Este método toma una hoja de sprites (spritesheets) y la divide en sprites individuales,
        creando una lista de superficies. La cantidad de filas y columnas, junto
        con el paso (step), determinan cuántos sprites se obtienen. Si flip es True,
        los sprites se voltearán horizontalmente.
        """
        sprites_list = []  # Crea una lista para almacenar las superficies
        surface_img = pygame.image.load(img_path)  # Carga la imagen y obtiene la superficie
        frame_width = int(surface_img.get_width() / cols)  # Calcula el ancho de un sprite
        frame_height = int(surface_img.get_height() / rows)  # Calcula el alto de un sprite

        for row in range(rows):  # Recorre las filas
            for column in range(0, cols, step):  # Recorre las columnas
                x_axis = column * frame_width  # Calcula la posición en el eje X
                y_axis = row * frame_height  # Calcula la posición en el eje Y

                frame_surface = surface_img.subsurface(
                    x_axis, y_axis, frame_width, frame_height
                )  # Obtiene la superficie del sprite individual

                if flip:  # Voltea horizontalmente si se indica
                    frame_surface = pygame.transform.flip(frame_surface, True, False)

                sprites_list.append(frame_surface)  # Agrega la superficie a la lista

        return sprites_list