peliculas= {
  "1000" : {
    "titulo" : "Inception",
    "year" : 2010,
    "actores" : {
        "protagonista":"Leo Dicaprio",
        "coprotagonista":"Tom Hardy"
    }
  },
  "1001" : {
    "titulo" : "Interstellar",
    "year" : 2014
  }
}
print(type(peliculas))
for id, info in peliculas.items():
    print("\nID:", id)
    for key in info:
        if(type(info[key]) == dict):
            print("-----")
            for clave, actor in info[key].items():
                print(clave+ ':', actor)        
        else:
            print(key + ':', info[key])