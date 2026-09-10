from vehiculo import Vehiculo

# Crear un vehículo con patente y año
vehiculo1 = Vehiculo("AB1234", 2020)

# Marcarlo como ingresado al taller
vehiculo1.ingresar()

# Imprimir su patente, año y tarifa_hora()
print(f"Patente: {vehiculo1.patente}")
print(f"Año: {vehiculo1.anio}")
print(f"Tarifa por hora: {vehiculo1.tarifa_hora()}")
