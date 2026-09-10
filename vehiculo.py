# Definición de la clase Vehiculo
class Vehiculo:
    # Método constructor que inicializa los atributos de la instancia
    def __init__(self, patente: str, anio: int) -> None:
        # Asignación del atributo patente
        self.patente: str = patente
        # Asignación del atributo anio
        self.anio: int = anio
        # Inicialización automática del atributo de estado _en_taller en False
        self._en_taller: bool = False

    # Método para registrar el ingreso del vehículo al taller
    def ingresar(self) -> None:
        # Cambia el estado de _en_taller a True indicando que el vehículo está en el taller
        self._en_taller = True

    # Método para registrar la entrega del vehículo al cliente
    def entregar(self) -> None:
        # Cambia el estado de _en_taller a False indicando que el vehículo salió del taller
        self._en_taller = False

    # Método que retorna la tarifa por hora genérica
    def tarifa_hora(self) -> int:
        return 5000
