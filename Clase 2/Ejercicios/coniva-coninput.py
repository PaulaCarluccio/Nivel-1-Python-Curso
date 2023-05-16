#Dada la variable precio con un valor entero calcular su valor con IVA incluido (21%)
#Y mostrarlo en pantalla.
print("Ingrese el valor, amigo")
var_Precio = float(input())
alicuota = float(21)
var_calciva = var_Precio + ((var_Precio * alicuota)/100)
print("El iva es: " + str(var_calciva))