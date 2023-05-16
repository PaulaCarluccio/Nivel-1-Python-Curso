print("Escribe algo: ")
textillo = input()
def contar(t):
    cantidad = len(textillo)
    return (f"{t} tiene {cantidad} de caracteres")

print(contar(textillo))