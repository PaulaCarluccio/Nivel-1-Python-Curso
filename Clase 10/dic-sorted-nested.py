peliculas= {
  "1000" : {
    "titulo" : "Inception",
    "year" : 2010
  },
  "1001" : {
    "titulo" : "Interstellar",
    "year" : 2014
  },
  "1002" : {
    "titulo" : "Time Machine",
    "year" : 1960
  },  
  "1003" : {
    "titulo" : "Planet of the apes",
    "year" : 1968
  }   
}

ordenados = sorted(peliculas, key=lambda x: (peliculas[x]['year']))
print(ordenados)