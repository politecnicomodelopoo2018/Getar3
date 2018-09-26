from flask import Flask, redirect, request, render_template
from cliente import Cliente
from pelicula import Pelicula

app = Flask(__name__)

@app.route('/')
def Menu():
   return render_template('menu.html')

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        c = Cliente()
        c.dni = 'NULL'
        c.nombre = nombre
        c.apellido = apellido
        c.Dar_de_Alta_Cliente()
        return redirect('/log/' + nombre + "/" + apellido)
    else:
        return render_template('login.html')

@app.route('/log/<nombre>/<apellido>/')
def success(nombre,apellido):
    lista_peliculas = Pelicula.ListarPeliculas()
    return render_template('pelis.html', nombre=nombre, apellido=apellido, lista_peliculas=lista_peliculas)


if __name__ == '__main__':
   app.run(debug = True)





