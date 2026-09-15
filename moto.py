# Importa la clase base Vehiculo desde el módulo vehiculo.py
from vehiculo import Vehiculo

# Define la clase Moto que hereda de la clase base Vehiculo
class Moto(Vehiculo):
    # Implementación del método abstracto tarifa_hora para la clase Moto
    def tarifa_hora(self) -> int:
        # Retorna la tarifa por hora correspondiente a una moto
        return 20000
