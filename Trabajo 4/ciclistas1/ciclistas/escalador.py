from ciclistas.ciclista import Ciclista

class Escalador(Ciclista):
    def __init__(self, identificador, nombre, aceleracion_promedio, grado_rampa):
        super().__init__(identificador, nombre)
        self.__aceleracion_promedio = aceleracion_promedio
        self.__grado_rampa = grado_rampa

    def imprimir_tipo(self):
        return "Es un Escalador"
