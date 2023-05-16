m=int(input("Ingrese anio: "))

if(m >= 1930 and m <=2018 and m%4 == 2 and not(m >1938 and m < 1950)):    
    print("Se jugó")
else:
    print("NO Se jugó")    