#Obtener el mes (escribir su nombre en español) e indicar el número de días que tiene.
#Para el caso de febrero validar el año para indicar si tiene 28 o 29.
from datetime import datetime
m=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
diasmes=[31,28,31,30,31,30,31,31,30,31,30,31]
def meses():
    fecha= datetime.now()
    #anio=int(fecha.strftime("%Y"))
    #mes=int(fecha.strftime("%m"))-1
    anio = 2020
    mes = 1
    if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0) and mes == 1:
        print(" Mes: Febrero, Dias: 29 ")
    else:
        print(f"Mes: {m[mes]}, Dias: {diasmes[mes]}")
meses()    