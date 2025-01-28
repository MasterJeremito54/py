from ciclistas.ciclista import Ciclista

class Velocista(Ciclista):
    def __init__(self, identificador, nombre, potencia_promedio, velocidad_sprint):
        super().__init__(identificador, nombre)
        self.__potencia_promedio = potencia_promedio
        self.__velocidad_sprint = velocidad_sprint

    def imprimir_tipo(self):
        return "Es un Velocista"