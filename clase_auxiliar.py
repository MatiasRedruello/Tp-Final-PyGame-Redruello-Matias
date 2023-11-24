import random
class Lucky():
    @staticmethod
    def random_shooting_time():
        # Generar un valor aleatorio (0 o 1)
        value = random.choice([1000,2000,3000])
        # Si el valor es 1, devuelve True; de lo contrario, devuelve False
        return value    