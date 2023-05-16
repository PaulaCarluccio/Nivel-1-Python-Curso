def nomyape():
    print("Nombre: ")
    nombre = input()
    print("Apellido: ")
    apellido = input()    
    print(f"{nombre} {apellido}")
    print("Quier volver a cargar? ")
    si = input()
    if(si == "s"):
        nomyape()
    else:
        print("Adios")
nomyape()