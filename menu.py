from flask import Flask, redirect, request, render_template, session
from persona import Persona
from pelicula import Pelicula
from cine import Cine
from horario import Horario
from sala import Sala
from butaca import Butaca
from reserva import Reserva

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def Menu():
   return render_template('menu.html')

@app.route('/registroAdmin')
def registroAdmin():
    return render_template('registroAdmin.html')

@app.route('/AdminPelis')
def AdminPelis():
    lista_peliculas = Pelicula.ListarPeliculas()
    return render_template('AdminPelis.html',lista_peliculas=lista_peliculas)

@app.route('/DarDeBajaPelis',methods = ['GET'])
def DarDeBajaPelis():
    idpeli = request.form.get("pelicula")
    Pelicula.Dar_de_Baja_Pelicula(idpeli)
    return render_template('AdminPelis.html')

@app.route('/ModificarPelis',methods = ['GET'])
def ModificarPelis():
    idpeli = request.form.get("pelicula")
    P = Pelicula.InfoPeli(idpeli)
    Pelicula.Modificar_Pelicula()
    return render_template('AdminPelis.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/loginAction',methods = ['POST', 'GET'])
def loginAction():
    # validar Contraseña cualdo la haya
    session["dni"] = request.form.get("dni")
    return render_template('menu.html')

@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/signupAction',methods = ['POST', 'GET'])
def signupAction():
    p = Persona()
    p.nombre = request.form['nombre']
    p.apellido = request.form['apellido']
    p.Dar_de_Alta_Persona()
    return redirect('/')



@app.route('/Pelis')
def Pelis():
    p = Persona.ObtenerDatosPersona(session["dni"])
    lista_peliculas = Pelicula.ListarPeliculas()
    lista_cines = Cine.ListarCines()
    return render_template('pelis.html', p=p, lista_peliculas=lista_peliculas, lista_cines=lista_cines)

@app.route('/horarios',methods = ['POST','GET'])
def Fecha_Hora():
    idpeli = request.form["pelicula"]
    idcine = request.form['cine']
    datos_peli = Pelicula.InfoPeli(idpeli)
    datos_cine = Cine.InfoCine(idcine)
    lista_horarios = Cine.GetHorariosCine(idcine)
    return render_template('horarios.html', lista_horarios=lista_horarios, peli=datos_peli, cine=datos_cine)

@app.route('/butacas',methods = ['POST','GET'])
def butacas():
    idHorario = request.form['horarios']
    idpeli = request.form.get('idpeli')
    idcine = request.form.get('idcine')
    H = Horario.GetInfoHorarios(idHorario)
    S = Horario.GetSala_En_Horario(idHorario)
    lista_butacas = Sala.Listar_Butacas(S.idSala)
    return render_template('butacas.html',lista_butacas=lista_butacas, S=S, H=H, idpeli=idpeli, idcine=idcine)

@app.route('/reservas',methods = ['POST','GET'])
def reservas():
    idButaca = request.form['butacas']
    idpeli = request.form['idpeli']
    idhorario= request.form['idhorario']
    P = Pelicula.InfoPeli(idpeli)
    H = Horario.GetInfoHorarios(idhorario)
    B = Butaca.get_butaca(idButaca)
    R = Reserva()
    R.idReserva = 'NULL'
    R.Cliente_dni = session['dni']
    R.Horarios_idHorario = idhorario
    R.Horarios_Sala_idSala = H.Sala_idSala
    R.Pelicula_idPelicula = idpeli
    R.Dar_de_Alta_Reserva()
    return render_template('reservas.html', B=B, H=H, P=P, R=R)

@app.route('/ver_reservas')
def ver_reservas():
    dni = session['dni']
    Pe = Persona.ObtenerDatosPersona(dni)
    Peli = Reserva.PeliculaEnReserva(dni)
    lista_reservas = Reserva.ListarReservas(dni)
    return render_template('ver_reservas.html', Pe=Pe, lista_reservas=lista_reservas, Peli=Peli)

if __name__ == '__main__':
   app.run(debug = True)



# 1. RESERVA DE ENTRADA - GUARDAR EN db LA RESERVA (MOSTRAR SOLO LAS BUTACAS LIBRES)
# 2. VER RESERVAS ACTUALES DE USUARIO
# 3. ADMINISTRACION PARA AGREGAR MODIFICAR ELIMINAR PELICULAS

