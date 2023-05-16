lista=["Pollo","Asado","papas"]
#listamin = [item.lower() for item in lista]
listamin = []
for item in lista:
    listamin.append(item.lower())
comida=input("Que comida desea agregar: ").lower()
if listamin.count(comida) > 0:
    print('ya se encuentra')
else:
    lista.append(comida)
print(lista)