class Equipo:
    def __init__(self, nombre_equipo, pais):
        self.__nombre_equipo = nombre_equipo
        self.__pais = pais
        self.__ciclistas = []

    def agregar_ciclista(self, ciclista):
        self.__ciclistas.append(ciclista)

    def imprimir_equipo(self):
        print(f"Equipo: {self.__nombre_equipo}, País: {self.__pais}")
        for ciclista in self.__ciclistas:
            print(ciclista.imprimir())
