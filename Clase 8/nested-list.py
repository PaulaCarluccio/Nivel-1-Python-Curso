notas_cuatrimestre= [[10,7],[8,5],[5,6]]
print(notas_cuatrimestre)

for i in notas_cuatrimestre:
    print(type(i))
    print(i)


for notas in notas_cuatrimestre:
    for nota in notas:
        print(nota)
    print("-------")
