humanos = {'Carlos':40,
          'Ana':20,
          'Viviana':51,
          'Caro':30}

print("Ordenados x Key")
for key in sorted(humanos):
    print(key, humanos[key])

print("******************")
print("Guardarlos en variable ordenados")
print("******************")

ordenados = sorted(humanos.items())
for k,v in ordenados:
    print(k, v)