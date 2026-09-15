# Importa la clase base Vehiculo desde el módulo vehiculo.py
from vehiculo import Vehiculo

# Define la clase Auto que hereda de la clase base Vehiculo
class Auto(Vehiculo):
    # Implementación del método abstracto tarifa_hora para la clase Auto
    def tarifa_hora(self) -> int:
        # Retorna la tarifa por hora correspondiente a un auto
        return 30000
