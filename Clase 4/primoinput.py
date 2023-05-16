print("verificar si numero es primo")
num1=int(input("ingese numero: "))
if num1 == 2:
    print("el numero es primo")   
elif num1 >2:
    for i in range(2,2):
        if num1%i == 0:
            print("el numero no es primo")
            break
        else:
            continue
    else:
        print("El numero es primo")
else:
    print("el numero no es primo")