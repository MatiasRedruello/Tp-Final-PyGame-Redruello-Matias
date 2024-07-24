import random
import pygame
import sqlite3
class Suport():
    def __init__(self) -> None:
        self.existe_table = False
        self.nombre_archivo_sql = "tabla_posiciones.db"
        self.ingrese_nombre = True

        
    @staticmethod
    def random_shooting_time():
        # Generar un valor aleatorio (0 o 1)
        value = random.choice([500,1000,1500,2000,2500,3000])
        # Si el valor es 1, devuelve True; de lo contrario, devuelve False
        return value 
       
    @staticmethod # lo puedo usar sin instancial la clase
    def getSurfaceFromSpriteSheet(path,columnas,filas,flip=False, step = 1,scale=1):
        lista = []
        surface_imagen = pygame.image.load(path)
        fotograma_ancho = int(surface_imagen.get_width()/columnas)
        fotograma_alto = int(surface_imagen.get_height()/filas)
        fotograma_ancho_scaled = int(fotograma_ancho*scale)
        fotograma_alto_scaled = int(fotograma_alto*scale)
        x = 0
        
        for fila in range(filas):
            for columna in range(0,columnas,step):
                x = columna * fotograma_ancho
                y = fila * fotograma_alto
                surface_fotograma = surface_imagen.subsurface(x,y,fotograma_ancho,fotograma_alto)
                if(scale != 1):
                    surface_fotograma = pygame.transform.scale(surface_fotograma,(fotograma_ancho_scaled, fotograma_alto_scaled)).convert_alpha() 
                if(flip):
                    surface_fotograma = pygame.transform.flip(surface_fotograma,True,False).convert_alpha() 
                lista.append(surface_fotograma)
        return lista
    @staticmethod
    def getSurfaceFromSeparateFiles(path_format,from_index,quantity,flip=False,step = 1,scale=1,w=0,h=0,repeat_frame=1):
        lista = []
        for i in range(from_index,quantity+from_index):
            path = path_format.format(i)
            surface_fotograma = pygame.image.load(path)
            fotograma_ancho_scaled = int(surface_fotograma.get_rect().w * scale)
            fotograma_alto_scaled = int(surface_fotograma.get_rect().h * scale)
            if(scale == 1 and w != 0 and h != 0):
                surface_fotograma = pygame.transform.scale(surface_fotograma,(w, h)).convert_alpha()
            if(scale != 1):
                surface_fotograma = pygame.transform.scale(surface_fotograma,(fotograma_ancho_scaled, fotograma_alto_scaled)).convert_alpha() 
            if(flip):
                surface_fotograma = pygame.transform.flip(surface_fotograma,True,False).convert_alpha() 
            
            for i in range(repeat_frame):
                lista.append(surface_fotograma)
        return lista
    
    def crear_base_datos_sql(self)->None:
        """
        Parametros: None
        Funcion: Crea una base de datos.
        Retorna: None
        """
        
        with  sqlite3.connect(self.nombre_archivo_sql) as conexion:
            try:
                # Se puede pasar los datos de la tabla y armar distintas?
                # Se pasa como diccionarios de str?
                # Video pasaron los datos con el tipo de dato. En que cabia si los paso o no?
                sentencia = f""" create table score
                               (name TEXT,
                                score INTEGER)
                                """  
                conexion.execute(sentencia)
                print("Se creo la tabla")
            except  sqlite3.Error as e:
                print(f"Error al crear la tabla: {e}")

              
    def insertar_tabla_sql(self,nombre_archivo:str,name:str,score:int)->None:
        """
        Parametros: Path-> Ruta del archivo.
                    Nombre del archivo -> Como voy a llamr al archivo.
        Funcion: Inserta una tabla
        Retorna: None
        """
        with sqlite3.connect(f"{nombre_archivo}") as conexion:
           
                # Se puede pasar por parametros datos nuevos?
                # Se pasan como  listas? tuplas? diccionarios? Se puede pasar directamente?
                conexion.execute("""insert into score(name,score)
                                values(?,?)""",(f"{name}",f"{score}"))
                print("Se agregaron datos")         
                        
             
    def obtener_tabla_ordenada(self,nombre_archivo:str)->dict:
        """
        Obtener los datos ordenados de la tabla
        Retorna: Diccionario con nombres como clave y puntajes como valor
        """
        resultados = {}
        with sqlite3.connect(f"{nombre_archivo}") as conexion:
            
                cursor = conexion.execute("SELECT name, score FROM score ORDER BY score DESC")
                rows = cursor.fetchall()
                for row in rows:
                    nombre, puntaje = row
                    resultados[nombre] = puntaje
            
        return resultados

   
    def mostrar_base_de_datos(self, name: str, score: int):    
        if self.existe_table and self.ingrese_nombre :
            self.insertar_tabla_sql(self.nombre_archivo_sql,name,score)
            self.ingrese_nombre = False
            
          