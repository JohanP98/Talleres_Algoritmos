#Entradas
import math

lecturaanterior=int(input("Escriba el monto de la lectura electrica anterior:"))
lecturaactual=int(input("Escriba el monto de la lectura electrica actual:"))
kilovatio=int(input("Escriba el valor del kilovatio:"))

#Caja negra
montofinal=abs(lecturaactual-lecturaanterior)*kilovatio
#Salidas
print("El monto final a pagar será de:",montofinal,"COP")