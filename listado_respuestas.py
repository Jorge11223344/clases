from usuario import Usuario

class ListadoRespuestas:
    def __init__(self,usuario, listado_respuestas):
        self.__usuario = usuario
        self.__listado_respuestas = listado_respuestas

@property
def usuario(self):
    return self.__usuario

@property
def listado_respuestas(self):
    return self.__listado_respuestas

