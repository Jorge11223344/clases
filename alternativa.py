

class Alternativa:
    def __init__(self,contenido,ayuda=None):
        self.contenido = contenido
        self.ayuda = ayuda

    def mostrar(self):
        if self.ayuda:
            return f"{self.contenido} {self.ayuda} "
        return self.contenido