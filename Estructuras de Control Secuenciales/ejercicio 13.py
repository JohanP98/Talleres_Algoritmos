#Entradas
import math

n1=int(input("Escriba el numero de billetes de 50000 que hay:"))
n2=int(input("Escriba el numero de billetes de 20000 que hay:"))
n3=int(input("Escriba el numero de billetes de 10000 que hay:"))
n4=int(input("Escriba el numero de billetes de 5000 que hay:"))
n5=int(input("Escriba el numero de billetes de 2000 que hay:"))
n6=int(input("Escriba el numero de billetes de 1000 que hay:"))
n7=int(input("Escriba el numero de billetes de 500 que hay:"))
n8=int(input("Escriba el numero de billetes de 100 que hay:"))

#Caja negra
n1t=(n1*50000)
n2t=(n2*20000)
n3t=(n3*10000)
n4t=(n4*5000)
n5t=(n5*2000)
n6t=(n6*1000)
n7t=(n7*500)
n8t=(n8*100)
dinerototal=(n1t+n2t+n3t+n4t+n5t+n6t+n7t+n8t)

#salidas
print("En el banco hay un total de:",dinerototal,"COP")