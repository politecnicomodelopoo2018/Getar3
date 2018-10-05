from flask import Flask, redirect, request, render_template
from cliente import Cliente
from pelicula import Pelicula
from cine import Cine

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
        return redirect('/Pelis/' + nombre + "/" + apellido)
    else:
        return render_template('login.html')

@app.route('/Pelis/<nombre>/<apellido>/')
def Pelis(nombre,apellido):
    lista_peliculas = Pelicula.ListarPeliculas()
    return render_template('pelis.html', nombre=nombre, apellido=apellido, lista_peliculas=lista_peliculas)

@app.route('/cines',methods = ['GET'])
def Cines():
    nombrePeli = request.args.get('nombrePeli')
    P = Pelicula.InfoPeli(nombrePeli)
    lista_cines = Cine.ListarCines()
    return render_template('cines.html', lista_cines=lista_cines,P=P)

@app.route('/horarios',methods = ['GET'])
def Fecha_Hora():
    nombreCine = request.args.get('nombreCine')
    C = Cine.InfoCine(nombreCine)
    lista_horarios = Cine.GetHorariosCine(nombreCine)
    return render_template('horarios.html',lista_horarios=lista_horarios,C=C)

if __name__ == '__main__':
   app.run(debug = True)



# 1. RESERVA DE ENTRADA - GUARDAR EN db LA RESERVA (MOSTRAR SOLO LAS BUTACAS LIBRES)
# 2. VER RESERVAS ACTUALES DE USUARIO
# 3. ADMINISTRACION PARA AGREGAR MODIFICAR ELIMINAR PELICULAS
# 4. LOGIN DE USUARIO CON SESSION
