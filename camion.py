# Importa la clase base Vehiculo desde el módulo vehiculo.py
from vehiculo import Vehiculo

# Define la clase Camion que hereda de la clase base Vehiculo
class Camion(Vehiculo):
    # Implementación del método abstracto tarifa_hora para la clase Camion
    def tarifa_hora(self) -> int:
        # Retorna la tarifa por hora correspondiente a un camión
        return 40000
