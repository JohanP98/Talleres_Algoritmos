Algoritmo  Num_Invertido
	//entradas
	Escribir "escriba el n�mero de dos cifras	"
	leer dos_cifras
	//caja negra
	unidad<-dos_cifras MOD 10
	decena<-trunc(dos_cifras/10)
	//salidas
	Escribir "El invertido es:" unidad decena
FinAlgoritmo
