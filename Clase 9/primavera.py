#Primavera: obtener fecha actual. Decir cuántos días faltan o es primavera o cuantos dias pasaron desde primavera
#Primavera Hemisferio sur: 22 de septiembre - 21 de diciembre

from datetime import date

hoy = date.today()
#hoy = date(2020,12,5)
#hoy = date(2020,12,30)

def primavera(today):
    if today < date(today.year,9,21):
        falta = date(today.year,9,21) - today
        return f"Faltan {falta.days} días para la primavera."
    elif date(today.year,9,21) < today < date(today.year,12,21):
        return "Es primavera"
    elif today > date(today.year,12,21):
        pasaron = today - date(today.year,12,21)
        return f"Pasaron {pasaron.days} días desde la primavera."
    
print(primavera(hoy))