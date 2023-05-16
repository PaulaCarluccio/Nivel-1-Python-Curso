pais = input("Ingrese país: ")
if len(pais) >= 4:
    continente = input("Ingrese continente a/e: ")
    paises_america = ["Argentina","Perú","Chile","Uruguay","Bolivia"]
    paises_europa = ["España","Italia","Holanda"]
    if continente.lower() == "a":
        paises_america.append(pais)
        insertar = True
    elif continente.lower() == "e":
        paises_europa.append(pais)
        insertar = True
    else:
        print("Error en el continente")
        insertar = False

    if insertar:
        print("AMERICA")
        for pais in paises_america:
            print(pais)
        print("EUROPA")
        for pais in paises_europa:
            print(pais)        
else:
    print("Minimo 4 caracteres")