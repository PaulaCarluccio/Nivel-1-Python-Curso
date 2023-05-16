peliculas= {
  "1000" : {
    "titulo" : "Inception",
    "year" : 2010
  },
  "1001" : {
    "titulo" : "Interstellar",
    "year" : 2014
  }
}

peliculas["1001"].pop("year")
for id, info in peliculas.items():
    print("\nID:", id)
    for key in info:
        print(key + ':', info[key])