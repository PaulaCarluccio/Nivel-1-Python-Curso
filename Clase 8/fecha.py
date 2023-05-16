from datetime import datetime
semana=["Domingo","Lunes","Martes","Miercoles","Jueves","Viernes","Sabado"]
meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
def fecha():
    x = datetime.now()
    dia=semana[int(x.strftime("%w"))]
    mes=meses[int(x.strftime("%m"))-1]    
    print(f"Hoy es {dia} {x.strftime('%d')} de {mes} del {x.strftime('%Y')} ")
fecha()