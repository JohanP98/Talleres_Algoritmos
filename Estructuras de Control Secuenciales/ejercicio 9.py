#entradas
import math

salarioh=int(input("Escriba el precio de la hora del lugar donde trabaja:"))
horas=int(input("Escriba la cantidad de horas trabajadas:"))

#caja negra
salariobase=(salarioh*horas)
descuentofijo=(salariobase*0.20)
salarioneto=(salariobase-descuentofijo)

#salidas
print("El salarineto a obtener es de:",salarioneto)