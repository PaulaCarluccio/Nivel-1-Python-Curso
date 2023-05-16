#Es este año, el anterior o el siguiente
from datetime import date

hoy=date.today()
anio=int(input("ingrese año: "))
if hoy.year > anio:
    print("El año es anterior al actual")
elif hoy.year < anio:
    print("Su año es posterior al actual")
else:
    print("Su año es el actual")