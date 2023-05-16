nombres = ['Carlos','Laura','Elena','Rafael']
def nombrecortos(nombre):
    if(len(nombre)<=5):
        return True
    else:
        return False

nombres_c = list(filter(nombrecortos,nombres))
print(nombres_c)