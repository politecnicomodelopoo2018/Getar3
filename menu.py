from flask import Flask, redirect, request, render_template
from cliente import Cliente
from cine import Cine
from pelicula import Pelicula

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('menu.html')

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        usuario = request.form['nombre']
        usuario2 = request.form['apellido']
        c = Cliente()
        c.dni = 'NULL'
        c.nombre = usuario
        c.apellido = usuario2
        c.Dar_de_Alta_Cliente()
        return redirect('/success/' + usuario+"/" + usuario2)
    else:
       return render_template('login.html')

@app.route('/success/<nombre>/<apellido>/')
def success(nombre,apellido):
    return render_template('pelis.html', nombre=nombre, apellido=apellido)

@app.route('/pelis/')
def peliculas():
    ci = Cine()
  
    p = Pelicula()
    p.idPelicula = 'NULL'
    p.nombrePelicula = 'Avengers'
    p.genero = 'Accion'
    p.estrellas = 5
    ci.Agregar_pelicula(p)

    p1 = Pelicula()
    p1.idPelicula = 'NULL'
    p1.nombrePelicula = 'Proyecto X'
    p1.genero = 'Comedia'
    p1.estrellas = 4
    ci.Agregar_pelicula(p1)

    p2 = Pelicula()
    p2.idPelicula = 'NULL'
    p2.nombrePelicula = 'Daredevil'
    p2.genero = 'Accion'
    p2.estrellas = 1
    ci.Agregar_pelicula(p2)

    p3 = Pelicula()
    p3.idPelicula = 'NULL'
    p3.nombrePelicula = 'Invictus'
    p3.genero = 'drama'
    p3.estrellas = 4
    ci.Agregar_pelicula(p3)
    
    return render_template('pelis.html', lista_peliculas=ci.lista_peliculas)

@app.route('/cine/<nombrePelicula>/<genero>/<estrellas>/')
def ElegirCine(nombrePelicula,genero,estrellas):
    return render_template('cine.html', nombrePelicula=nombrePelicula, genero=genero, estrellas=estrellas)


if __name__ == '__main__':
   app.run(debug = True)


"""

ci = Cine()
p = Pelicula()
p.idPelicula = 'NULL'
p.nombrePelicula = 'Avengers'
p.genero = 'Accion'
p.estrellas = 5
ci.Agregar_pelicula(p)

p1 = Pelicula()
p1.idPelicula = 'NULL'
p1.nombrePelicula = 'Proyecto X'
p1.genero = 'Comedia'
p1.estrellas = 4
ci.Agregar_pelicula(p1)

p2 = Pelicula()
p2.idPelicula = 'NULL'
p2.nombrePelicula = 'Daredevil'
p2.genero = 'Accion'
p2.estrellas = 1
ci.Agregar_pelicula(p2)

p3 = Pelicula()
p3.idPelicula = 'NULL'
p3.nombrePelicula = 'Invictus'
p3.genero = 'drama'
p3.estrellas = 4
ci.Agregar_pelicula(p3)
    

for item in ci.lista_peliculas:
    print(item.nombrePelicula)
    print("")
"""


