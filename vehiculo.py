# Importa ABC y abstractmethod para definir clases y métodos abstractos
from abc import ABC, abstractmethod

# Definición de la clase base Vehiculo como clase abstracta
class Vehiculo(ABC):
    # Método constructor que inicializa los atributos al crear una instancia
    def __init__(self, patente: str, anio: int) -> None:
        # Asignación del parámetro patente al atributo de la instancia
        self.patente: str = patente
        # Asignación del parámetro anio al atributo de la instancia
        self.anio: int = anio
        # Inicialización del atributo privado de estado _en_taller en False
        self._en_taller: bool = False

    # Método para registrar el ingreso del vehículo al taller mecánico
    def ingresar(self) -> None:
        # Cambia el estado interno a True indicando que el vehículo está dentro del taller
        self._en_taller = True

    # Método para registrar la entrega y salida del vehículo al cliente
    def entregar(self) -> None:
        # Cambia el estado interno a False indicando que el vehículo ha salido del taller
        self._en_taller = False

    # Método abstracto que cada subclase debe implementar para definir su tarifa por hora
    @abstractmethod
    def tarifa_hora(self) -> int:
        pass
