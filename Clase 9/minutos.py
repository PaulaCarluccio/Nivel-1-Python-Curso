#Pedir al usuario que ingrese una cantidad de minutos. Crear una función para convertir a días, horas, minutos.


def minute(minutos):
    print(f"{int((minutos/60)/24)} dias")
    print(f"{int(((minutos/60)%24))} horas")
    print(f"{int(minutos%60)} mins")

minute(int(input("Ingrese la cantidad de minutos: ")))