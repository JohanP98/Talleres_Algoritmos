Algoritmo vehiculos
	//entradas
	Escribir "Escriba la velocidad en km del primer vehiculo"
	Leer v1
	Escribir "Escriba la velocidad en km del segundo vehiculo"
	Leer v2
	Escribir "Escriba la distancia que tenian un vehiculo del otro"
	Leer d
	//caja negra
	Diferencia_de_velocidad<-(v2-v1)
	tiempo<-d/Diferencia_de_velocidad
	tiempo_min<-tiempo*60
	//salidas
	Escribir "El segundo vehiculo alcanzará al primero en: " tiempo_min " minutos" 
	
FinAlgoritmo