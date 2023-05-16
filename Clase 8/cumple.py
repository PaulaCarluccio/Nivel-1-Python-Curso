#pau
cumple_user = input("Ingrese su cumpleaños: DD/MM/AAAA -------> ")

cumple = cumple_user.split("/")

dia = int(cumple[0])
mes = int(cumple[1])
anio = int(cumple[2])


from datetime import date

def calculateAge(birthDate):
    today = date.today()    
    if today < birthDate:
        return "No se puede calcular"
    else:
        age = today.year - anio - ((today.month, today.day) < (mes, dia))   
        return age
print(calculateAge(date(anio, mes, dia)), "años")