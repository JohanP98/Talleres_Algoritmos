#entradas
LecturaA=int(input("Escriba el valor de la lectura anterior:"))
LecturaAA=int(input("Escriba el valor de la lectura actual:"))

#caja negra
diferencia=(LecturaA-LecturaAA)

#----Kwh-----
monto=""
if(0<=diferencia<=100):
    kwh=4600
elif(101<=diferencia<=300):
    kwh=80
elif(301<=diferencia<=500):
    kwh=100000
elif(diferencia>=501):
    kwh=120000

monto=(diferencia*kwh)
print("el monto a pagar por concepto de consumo de luz electrica y servici de aseo urbano es de:",monto,"COP")