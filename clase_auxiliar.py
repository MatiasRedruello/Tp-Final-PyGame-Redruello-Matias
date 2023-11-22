import random
class Suport():
    @staticmethod
    def propiedad_aleatoria():
        # Generar un valor aleatorio (0 o 1)
        valor = random.choice([1000,2000,3000])
        # Si el valor es 1, devuelve True; de lo contrario, devuelve False
        return valor    