from datetime import date  
def calculateAge(birthDate):     
    today = date.today()
    print(type(today))
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))   
    return age
print(calculateAge(date(1980, 5, 5)), "años") 