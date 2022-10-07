#entradas
import math

Sueldo=float(input("Ingrese el sueldo:"))
v1=float(input("Ingrese el costo de la primera venta:"))
v2=float(input("Ingrese el costo de la segunda venta:"))
v3=float(input("Ingrese el costo de la tercera venta:"))

#caja negra
totalventas=(v1+v2+v3)
comisión=(totalventas*0.10)
dinerototalmes=(Sueldo+comisión)

#salidas
print("El dinero obtenido por concepto de comisiones es de:",comisión, "y el total de dinero a obtener a final de mes es:",dinerototalmes)