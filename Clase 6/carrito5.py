carrito = []
preguntar = True
while len(carrito) < 5 and preguntar:
    a=input("Desea cargar un item? s/n: ").lower()
    if a == "s":
        carrito.append(int(input("Ingrese item a cargar: ")))
    elif a !="s":
        print("No se cargaran mas items")
        preguntar = False
        
print("Lista Productos")
for item in carrito:
    print(item)
cantidad = len(carrito)
print(f"Usted cargo un total de {cantidad} productos")
print("La suma de sus productos es: ",sum(carrito))