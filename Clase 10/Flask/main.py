from flask import Flask
app = Flask(__name__)
@app.route("/")
def presentar_www():
    return "<h1>Hola, mi nombre es Dami.<h1><img src='https://via.placeholder.com/300/09f/fff.png'>"

@app.route("/notas")
def notas_www():
    notas= [[10,7],[8,5],[5,6]]
    acumula = ''
    for nota in notas:
        acumula = acumula + str(nota) + " - "
    return acumula

@app.route('/buscar/')
def buscar():    
    return """
        <form action="/buscar" method="get">    
            <input type="search" name="buscar">
            <input type="search" name="buscar2">
            <input type="submit" value="Buscar">
        </form>
    """ 