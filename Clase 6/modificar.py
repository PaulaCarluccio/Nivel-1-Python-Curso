nombres = ["Pablo","Marcos","Ernesto","Elias","Victoria","Lidia"]
buscar = input("Qué nombre quiere buscar?")
if buscar in nombres:
    i = nombres.index(buscar)    
    nombres[i] = input("Por qué nombre desea reemplazarlo?:")
    print(nombres)
else:
    print("No se encuentra el nombre en la lista")   