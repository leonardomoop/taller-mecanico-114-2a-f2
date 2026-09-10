# Definición de la clase base Vehiculo
class Vehiculo:
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

    # Método que calcula y retorna el costo por hora del vehículo
    def tarifa_hora(self) -> int:
        # Retorna el monto genérico de 5000 pesos por hora
        return 5000
