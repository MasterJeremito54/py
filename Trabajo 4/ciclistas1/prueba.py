from ciclistas.velocista import Velocista
from ciclistas.escalador import Escalador
from ciclistas.contrarrelojista import Contrarrelojista
from equipo.equipo import Equipo

if __name__ == "__main__":
    # Crear ciclistas
    velocista = Velocista(1, "Carlos", 400, 70)
    escalador = Escalador(2, "Ana", 3.5, 25)
    contrarrelojista = Contrarrelojista(3, "Luis", 60)

    # Crear equipo y agregar ciclistas
    equipo = Equipo("Team Mojon", "Colombia")
    equipo.agregar_ciclista(velocista)
    equipo.agregar_ciclista(escalador)
    equipo.agregar_ciclista(contrarrelojista)

    equipo.imprimir_equipo()
