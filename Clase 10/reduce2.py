from functools import reduce

peliculas = [{"titulo":"Inception","director":"Nolan"},{"titulo":"Star Wars","director":"George Lucas"}]

def transformar(coleccion, peli):
    coleccion[peli["titulo"]] = peli["director"]
    return coleccion
 
diccionario = reduce(transformar,peliculas,{})
print(diccionario)
print(type(diccionario))
print(type(peliculas))