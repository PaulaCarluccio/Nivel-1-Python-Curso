notas_cuatrimestre = [[10,5],[8,5],[5,6]]

for notas in notas_cuatrimestre:    
    a = 1
    for nota in notas:        
        print(f"Cuatrimestre {a}: {nota}")
        a = a+1
    print("-------------")