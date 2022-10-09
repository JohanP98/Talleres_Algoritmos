#Entradas
nombre=(input("Escriba su nombre: "))
horasdia=int(input("Escriba el numero de horas que trabajó al día: "))
dias=int(input("Escriba la cantidad de dias que trabajó en el mes: "))
valorhorasn=int(input("Escriba lo que le pagan por uan hora normal: "))
horase=int(input("Escriba el numero de horas extra que trabajó en el mes:"))
hijos=int(input("Escriba el numero de hijos que tiene:"))
#Caja negras
horas=horasdia*dias
porcentajehe=valorhorasn*0.25
valorhe=valorhorasn+porcentajehe
pagohorasn=horas*valorhorasn
pagohe=horase*valorhe
salariobase=pagohe+pagohorasn
descuento1=salariobase*0.05
descuento2=salariobase*0.02
descuento3=salariobase*0.07
deducciontotal=(descuento1+descuento2+descuento3)
dinerohijos=hijos*173000
asignaciontotal=(dinerohijos+250000+180000)
salarioneto=salariobase-deducciontotal+asignaciontotal
#Salidas
print ("Su salario base es de $",salariobase,"COP")
print ("El dinero de la deducción en total es de: $",deducciontotal,"COP")
print ("El dinero de la asignación en total es de: $",asignaciontotal,"COP")
print (nombre,"su salario neto es de $:",salarioneto,"COP")
