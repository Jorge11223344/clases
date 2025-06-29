from pregunta import Pregunta

class Encuesta:

    def __init_(self, nombre, preguntas):
        self.nombre = nombre
        self.__preguntas = preguntas
        self.__listado_respuestas = []

    @property
    def preguntas(self):
        return self.__preguntas
    
    @property
    def listado_respuestas(self):
        return self.__listado_respuestas

    def mostar_encuesta(self):
        pass

    def agregar_listado_respuestas(self):
        pass
                  
class EncuestaLimitadaEdad(Encuesta):
    def __init__(self,nombre,preguntas,edad_min, edad_max):
        super().__init__(nombre,preguntas)
        self.__edad_min =edad_min
        self.__edad_max = edad_max

    @property
    def edad_min(self):
        return self.__edad_min
    
    @edad_min.setter
    def edad_min(self, nueva_edad_min):
        self.__edad_min = nueva_edad_min

    @property
    def edad_max(self):
        return self.__edad_max
    
    @edad_max.setter
    def edad_min(self, nueva_edad_max):
        self.__edad_max = nueva_edad_max


    def agregar_listado_respuestas(self,listado):
        pass

class EncuestaLimitadaRegion(Encuesta):
    def __init__(self,nombre, preguntas, lista_regiones):
        super().__init__(nombre,preguntas)
        self.__regiones = lista_regiones

    @property
    def regiones(self):
        return self.__regiones
    
    @regiones.setter
    def regiones(self,nuevas_regiones):
        self.__regiones = nuevas_regiones

    def agregar_listado_respuestas(self,listado):
        pass




