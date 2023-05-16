decidir = "s"
comidas = ["Pollo","Pizza","Asado","Pastas"]
while decidir == "s":
    comida = input("Comida? ")
    comidas.append(comida)
    print(comidas)
    decidir = input("Otra comida s/n? ")
    if decidir != "s":
        break