#entradas
A=int(input())
B=int(input())
C=int(input())
D=int(input())
#caja negra

operación=""
if(D==0):
    operación=(A-C)**2
    print("el resultado es:",operación)
elif(D>0):
    operación=((A-B)**3)/D
    print("el resultado es:",operación)
else:
    print("none")

