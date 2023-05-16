borrar = input("Que quitamos? ").lower()
comidas = ['Pollo', 'Pizza', 'Asado', 'Pastas', 'Pollo',"Asado"]
for c in comidas:
    if borrar  == c.lower():
        comidas.remove(c)
print(comidas)