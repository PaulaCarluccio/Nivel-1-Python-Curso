from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
hoy = date.today()
ayer = hoy - timedelta(days=1) 
maniana = hoy + timedelta(days=1) 
diferencia_en_dias = maniana - hoy
print(hoy)

hoy = datetime.today()
antes = hoy - timedelta(seconds=60) 
despues = hoy + timedelta(seconds=60) 
print(despues-antes)