#Dadas las notas de 4 bimestres de un alumno mostrar el promedio
#Indicar si aprobó (se aprueba con 7). Las notas están en 4 variables distintas.

b1 = 10
b2 = 6
b3 = 7
b4 = 9
#promedio = b1+b2+b3+b4/4
#promedio = int(b1+b2+b3+b4)/4
promedio = (int(b1)+int(b2)+int(b3)+int(b4))/4
print(promedio)
if promedio > 7:
    print ("Aprobado") 
else:
    print ("Desaprobado")