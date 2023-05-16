from datetime import datetime, date, time, timedelta

hoy = date.today()
tomorrow = hoy + timedelta(days=1)
diferencia_en_dias = tomorrow - hoy
print(diferencia_en_dias)

ahora = datetime.now()
print(ahora)
dentrode2 = ahora + timedelta(seconds = 120)
print(dentrode2)
fecha2 = datetime(1995, 11, 5, 0, 0, 0)
diferencia = ahora - fecha2
print(diferencia)
navidad = date(2020, 12, 25)
print(navidad)
faltan_para_navidad = navidad - hoy
print(faltan_para_navidad)