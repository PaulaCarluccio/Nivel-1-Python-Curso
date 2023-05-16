from datetime import timedelta
def mins_a_dhm():
    mins=int(input("ingrese la cantidad de minutos: "))
    f=timedelta(minutes=mins)
    print(f)
mins_a_dhm()