# Mostrar lo años desde este año (obtenerlo) hasta 50 años para atrás (de 1 en 1 con for o while)
from datetime import datetime
fecha=datetime.now()
anio=int(fecha.strftime("%Y"))
for x in range(anio,anio-51,-1):
    print(x)    