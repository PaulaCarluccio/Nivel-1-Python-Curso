print("Elija la inicial: ")
inicial = input()
paises=["Argentina","Brasil","Chile","Alemania","Argelia","España","Francia","Albania","Colombia"]
contador = 0
for pais in paises:
    if pais.lower()[0] == inicial.lower() and contador < 2:
        print(pais)
        contador = contador+1
if contador == 0:
    print("No contrado")