Algoritmo Sueldo_y_comisiones
	//entradas
	Escribir "Escriba su sueldo"
	Leer sueldo
	Escribir "Escriba el costo total de las 3 ventas realizadas en el mes"
	Leer vt
	//caja negra
	comisión<-(vt*0.1)
	din_total<-sueldo+comisión
	//salidas
	Escribir " El dinero obtenido de las comisiones es:" comisión "El total del dinero a recibirse a final de mes:" din_total
FinAlgoritmo
