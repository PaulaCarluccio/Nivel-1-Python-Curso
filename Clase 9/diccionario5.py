pelicula = {
  "titulo": "Inception",
  "director": "Nolan",
  "year": 2010
}


if(pelicula["year"] == 2010):
    print("Se estrenó en 2010")
else:
    print("NO se estrenó en 2010")
    
pelicula["actor"] = "Leo Dicaprio"
pelicula.pop("year")
print(pelicula)