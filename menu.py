from flask import Flask, redirect, url_for, request, render_template
from cliente import Cliente
from cine import Cine

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
    return render_template('pelis.html', nombre = nombre, apellido = apellido)

@app.route('/pelis/<pelicula>/<lista_peliculas>/')
def peliculas(pelicula):
    ci = Cine()
    return render_template('pelis.html',pelicula = pelicula, lista_peliculas = ci.lista_peliculas)

if __name__ == '__main__':
   app.run(debug = True)

