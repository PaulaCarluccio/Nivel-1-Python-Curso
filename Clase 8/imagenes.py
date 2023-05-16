imagenes = [["https://via.placeholder.com/300.png/f9f/fff","Rosa"],["https://via.placeholder.com/300.png/09f/fff","Celeste"]]

# Link de html <img src="imagen.png"><br>Texto<br>

for imagen in imagenes:
    print(f'<img src="{imagen[0]}"><br>{imagen[1]}<br>')
