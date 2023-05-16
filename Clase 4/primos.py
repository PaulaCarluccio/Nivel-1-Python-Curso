#primos del 2 al 10
for x in range (2,10,1):
    for i in range(2,x,1):
        if x%i == 0:
            break
        else:
            continue
    else:
        print(x)