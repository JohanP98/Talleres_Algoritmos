#entradas
import math

A=int(input())
B=int(input())
C=int(input())
D=int(input())

#caja negra
miles=(A*1000)
centenas=(B*100)
decenas=(C*10)
dosdigitos=(decenas+D)

operacion=miles+centenas+dosdigitos

def round_up(operacion, decimals = 0):
    multiplier = 10 ** decimals
    return math.ceil(operacion*multiplier)/multiplier
def round_down(operacion, decimals = 0):
    multiplier = 10 ** decimals
    return math.floor(operacion*multiplier)/multiplier
op=""
if(dosdigitos<50):
    op=(round_down(operacion,-2))
    print(op)
elif(dosdigitos>=50):
    op=(round_up(operacion,-2))
    print(op)
