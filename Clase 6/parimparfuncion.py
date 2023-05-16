print("Dime un numero, amigo")
n = input()
def par(x):
    if int(x)%2 == 0:
        return True
    else:
        return False
validar = par(n)

print(validar)

if (validar == True):
    print("Par")
else:
    print("NO Par")    