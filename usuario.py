


class Usuario:
    def __init__(self, email,edad,region):
        self.__email = email
        self.__edad = edad
        self.__region = region

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email_nuevo):
        self.__email = email_nuevo
    
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, edad_nuevo):
        self.__edad = edad_nuevo

    @property
    def region(self):
        return self.__region
    
    @region.setter
    def region(self, region_nuevo):
        self.__region = region_nuevo

    def contestar_encuesta(self):
        pass
