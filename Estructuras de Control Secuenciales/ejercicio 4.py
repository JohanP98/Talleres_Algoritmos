#entradas
import math
Compra=float(input("Escriba el valor de su compra para saber el total a pagar con descuento:"))

#caja negra
valordescuento=(Compra*0.15)
totalpagar=(Compra-valordescuento)

#salidas
print("Su valor a pagar al final con el descuento sera de:", totalpagar)