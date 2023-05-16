
#Calcular cuántas horas, minutos y segundos faltan para terminar el día.
from datetime import datetime
fecha= datetime.now()
print(f"""Faltan
{23-int(fecha.strftime('%H'))} Horas
{59-int(fecha.strftime('%M'))} Minutos
{59-int(fecha.strftime('%S'))} Segundos
Para finalizar el dia""")