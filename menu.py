from flask import Flask, redirect, request, render_template
from persona import Persona
from pelicula import Pelicula
from cine import Cine
from horario import Horario
from sala import Sala
from reserva import Reserva

app = Flask(__name__)

pepe = 0

@app.route('/')
def Menu():
   return render_template('menu.html')

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        p = Persona()
        p.dni = 'NULL'
        p.nombre = nombre
        p.apellido = apellido
        pepe = p.Dar_de_Alta_Persona().lastrowid

        return redirect('/Pelis/' + nombre + "/" + apellido)
    else:
        return render_template('login.html')

@app.route('/Pelis/<nombre>/<apellido>/')
def Pelis(nombre,apellido):
    lista_peliculas = Pelicula.ListarPeliculas()
    lista_cines = Cine.ListarCines()
    return render_template('pelis.html', nombre=nombre, apellido=apellido, lista_peliculas=lista_peliculas, lista_cines=lista_cines)

@app.route('/horarios',methods = ['POST','GET'])
def Fecha_Hora():
    peli = request.form.get("pelicula")
    idCine = request.form['cine']
    lista_horarios = Cine.GetHorariosCine(idCine)
    return render_template('horarios.html', lista_horarios=lista_horarios)

@app.route('/butacas',methods = ['POST','GET'])
def butacas():
    fecha_hora = request.form['horarios']
    S = Horario.GetSala_En_Horario(fecha_hora)
    lista_butacas = Sala.Listar_Butacas(S.idSala)
    return render_template('butacas.html',lista_butacas=lista_butacas,S=S)

@app.route('/reservas',methods = ['GET'])
def reservas():

    """
    R = Reserva()
    R.idReserva = 'NULL'
    R.Cliente_dni = pepe
    R.Horarios_idHorario = idHorario
    R.Horarios_Sala_idSala = idSala
    R.Pelicula_idPelicula = idPeli
    R.Dar_de_Alta_Reserva()
    """
    return 0

if __name__ == '__main__':
   app.run(debug = True)



# 1. RESERVA DE ENTRADA - GUARDAR EN db LA RESERVA (MOSTRAR SOLO LAS BUTACAS LIBRES)
# 2. VER RESERVAS ACTUALES DE USUARIO
# 3. ADMINISTRACION PARA AGREGAR MODIFICAR ELIMINAR PELICULAS
# 4. LOGIN DE USUARIO CON SESSION
