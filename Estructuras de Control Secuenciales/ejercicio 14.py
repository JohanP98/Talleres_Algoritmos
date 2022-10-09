#Entradas
import math

lecturaanterior=int(input("Escriba el monto de la lectura electrica anterior:"))
lecturaactual=int(input("Escriba el monto de la lectura electrica actual:"))
kilovatio=int(input("Escriba el valor del kilovatio:"))
montoanterior=int(input("Escriba el monto que se pagó en el mes anterior"))

#Caja negra
montoadicional=abs(lecturaanterior-lecturaactual)*kilovatio
montofinal=(lecturaactual*kilovatio)
#Salidas
print("El monto que se adiciona al monto del mes anterior es de:",montoadicional,"COP")
print("El monto final a pagar será de:",montofinal,"COP")