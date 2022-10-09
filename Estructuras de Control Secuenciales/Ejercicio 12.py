#Entradas
import math

tareaquim1=int(input("Escriba la nota obtenidad en la tarea 1 de quimica:"))
tareaquim2=int(input("Escriba la nota obtenidad en la tarea 2 de quimica:"))
tareaquim3=int(input("Escriba la nota obtenidad en la tarea 3 de quimica:"))
examenquim=int(input("Escriba la nota obtenida en el examen de quimica:"))
tareafis1=int(input("Escriba la nota obtenidad en la tarea 1 de fisica:"))
tareafis2=int(input("Escriba la nota obtenidad en la tarea 2 de fisica:"))
tareafis3=int(input("Escriba la nota obtenidad en la tarea 3 de fisica:"))
examenfis=int(input("Escriba la nota obtenida en el examen de fisica:"))
tareamat1=int(input("Escriba la nota obtenidad en la tarea 1 de matematicas:"))
tareamat2=int(input("Escriba la nota obtenidad en la tarea 2 de matematicas:"))
tareamat3=int(input("Escriba la nota obtenidad en la tarea 3 de matematicas:"))
examenmat=int(input("Escriba la nota obtenida en el examen de matematicas:"))

#caja negra
promtareasmat=(tareamat1+tareamat2+tareamat3)/3
porcentajetareasmat=(promtareasmat*0.10)
porcentajeexamenmat=(examenmat*0.90)
promediofinalmat=(porcentajeexamenmat+porcentajetareasmat)

promtareasfis=(tareafis1+tareafis2+tareafis3)/3
porcentajetareasfis=(promtareasfis*0.20)
porcentajeexamenfis=(examenfis*0.80)
promediofinalfis=(porcentajetareasfis+porcentajeexamenfis)

promediotareasquim=(tareaquim1+tareaquim2+tareaquim3)/3
porcentajetareasquim=(promediotareasquim*0.15)
porcentajeexamenquim=(examenquim*0.85)
promediofinalquim=(porcentajetareasquim+porcentajeexamenquim)

promediofinaltotal=(promediofinalquim+promediofinalmat+promediofinalfis)/3

#Salidas
print("El promedio en la materia de matematicas es de:",promediofinalmat)
print("El promedio en la materia de fisica es de:",promediofinalfis)
print("El promedio en la materia de quimica es de:",promediofinalquim)
print("El promedio final entre las tres materias es de:",promediofinaltotal)