humanos = {'Carlos':40,
          'Ana':20,
          'Viviana':51,
          'Caro':30}

ordenados = sorted(humanos.items(), key=lambda x: x[1])

print(type(humanos))
print(ordenados)
for k,v in ordenados:
    print(k, v)