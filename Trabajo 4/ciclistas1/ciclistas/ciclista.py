from abc import ABC, abstractmethod

class Ciclista(ABC):
    def __init__(self, identificador, nombre):
        self.__identificador = identificador
        self.__nombre = nombre
        self.__tiempo_acumulado = 0  # Inicializado en 0

    @abstractmethod
    def imprimir_tipo(self):
        """Método abstracto para imprimir el tipo de ciclista"""
        pass

    def imprimir(self):
        return f"Ciclista ID: {self.__identificador}, Nombre: {self.__nombre}, Tiempo Acumulado: {self.__tiempo_acumulado} min"

    
    def get_identificador(self):
        return self.__identificador

    def get_nombre(self):
        return self.__nombre

    def get_tiempo_acumulado(self):
        return self.__tiempo_acumulado

    def set_tiempo_acumulado(self, tiempo):
        self.__tiempo_acumulado = tiempo