import json

class Archivo():
    @staticmethod
    def leer_json(ruta: str, modo: str, nivel: str) -> list[dict]:

        with open(ruta, modo, encoding='utf-8') as archivo_json:
            level_setting = json.load(archivo_json).get(nivel)[0]
        return level_setting
    
    def crear_lista_caracteristicas(ruta: str, modo: str, nivel: str,clase_deseada):
        archivo_json = Archivo.leer_json(ruta, modo, nivel)
        lista_vacia = []
        for clave in archivo_json.get(f"{clase_deseada}").values():
            lista_vacia.append(clave)    
        return lista_vacia    