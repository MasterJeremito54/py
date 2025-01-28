from ciclistas.ciclista import Ciclista

class Contrarrelojista(Ciclista):
    def __init__(self, identificador, nombre, velocidad_maxima):
        super().__init__(identificador, nombre)
        self.__velocidad_maxima = velocidad_maxima

    def imprimir_tipo(self):
        return "Es un Contrarrelojista"
