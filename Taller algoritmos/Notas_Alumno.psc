Algoritmo Notas_Alumno
	Escribir'Nota promedio de calificaciones parciales:'
	Leer n1
	Escribir'Nota del examen final:'
	Leer n2
	Escribir'Nota del trabajo final:'
	Leer n3
	
	porcen55<-trunc(n1*0.55)
	porcen30<-trunc(n2*0.30)
	porcen15<-trunc(n3*0.15)
	
	nf<-trunc(porcen55+porcen30+porcen15)
	
	Escribir "Su nota final es: " nf
	
FinAlgoritmo
