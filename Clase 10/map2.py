nombres = ['Carlos','Laura','Elena','Rafael']
def pasar_a_mayusculas(nombre):
    return str(nombre).upper()

nombres_may = list(map(pasar_a_mayusculas,nombres))
print(nombres_may)