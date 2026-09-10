# Importa la clase base Vehiculo desde el módulo vehiculo.py
from vehiculo import Vehiculo

# Instancia un objeto de tipo Vehiculo pasando patente y año de fabricación
vehiculo1 = Vehiculo("AB1234", 2020)

# Llama al método ingresar() para cambiar el estado del vehículo a dentro del taller
vehiculo1.ingresar()

# Define una variable de texto con el mensaje de confirmación de ingreso
mensaje = "Vehículo ingresado exitosamente al taller para revisión."

# Imprime en consola la patente del vehículo accediendo a su atributo
print(f"Patente: {vehiculo1.patente}")

# Imprime en consola el año de fabricación accediendo a su atributo
print(f"Año: {vehiculo1.anio}")

# Imprime en consola el costo por hora ejecutando el método tarifa_hora()
print(f"Tarifa por hora: {vehiculo1.tarifa_hora()}")

# Imprime en consola el mensaje de estado almacenado en la variable
print(f"Mensaje: {mensaje}")
