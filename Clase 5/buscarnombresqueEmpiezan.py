inicial = input("Inicial")
while len(inicial) > 1:
    print("Error")
    inicial = input("Inicial")
nombres = ["Ana","alberto","Carlos","Fabricio","Analia","Fernando","Anastacia"]
for nombre in nombres:
    primera = nombre.lower().startswith(inicial.lower())
    if  primera:
        print(nombre)