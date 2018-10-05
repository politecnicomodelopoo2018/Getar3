from flask import Flask, redirect, request, render_template
from cliente import Cliente
from pelicula import Pelicula
from cine import Cine
from horario import Horario
from sala import Sala
from reserva import Reserva

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
    lista_cines = Cine.ListarCines()
    """
    C = Cine.InfoCine()
    lista_horarios = Cine.GetHorariosCine()
    """
    return render_template('pelis.html', nombre=nombre, apellido=apellido, lista_peliculas=lista_peliculas, lista_cines=lista_cines)
"""
@app.route('/cines',methods = ['GET'])
def Cines():
    nombrePeli = request.args.get('nombrePeli')
    P = Pelicula.InfoPeli(nombrePeli)
    lista_cines = Cine.ListarCines()
    return render_template('cines.html', lista_cines=lista_cines,P=P)
"""
@app.route('/horarios',methods = ['GET'])
def Fecha_Hora():
    nombreCine = request.args.get('nombreCine')
    C = Cine.InfoCine(nombreCine)
    lista_horarios = Cine.GetHorariosCine(nombreCine)
    return render_template('horarios.html',lista_horarios=lista_horarios,C=C)

@app.route('/butaca',methods = ['GET'])
def fecha_Hora():
    fecha_hora = request.args.get('fecha_hora')
    H = Horario.GetInfoHorarios(fecha_hora)
    S = Horario.GetSala_En_Horario(fecha_hora)
    lista_butacas = Sala.Listar_Butacas(S.idSala)
    return render_template('butacas.html',lista_butacas=lista_butacas,H=H,S=S)

@app.route('/reservas',methods = ['GET'])
def reservas():
    dni = request.args.get['dni']
    idPeli = request.args.get['idPelicula']
    idSala = request.args.get['idSala']
    idHorario = request.args.get['idHorario']
    R = Reserva()
    R.idReserva = 'NULL'
    R.Cliente_dni = dni
    R.Horarios_idHorario = idHorario
    R.Horarios_Sala_idSala = idSala
    R.Pelicula_idPelicula = idPeli
    R.Dar_de_Alta_Reserva()


if __name__ == '__main__':
   app.run(debug = True)



# 1. RESERVA DE ENTRADA - GUARDAR EN db LA RESERVA (MOSTRAR SOLO LAS BUTACAS LIBRES)
# 2. VER RESERVAS ACTUALES DE USUARIO
# 3. ADMINISTRACION PARA AGREGAR MODIFICAR ELIMINAR PELICULAS
# 4. LOGIN DE USUARIO CON SESSION
