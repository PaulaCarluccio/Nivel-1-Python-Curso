borrar = input("Qué borro? ")
comidas = ["Pollo","Pizza","Asado","Pastas"]
if comidas.count(borrar) == 0:
    print("Error, no existe la comida")
else:
    comidas.remove(borrar)
print(comidas)