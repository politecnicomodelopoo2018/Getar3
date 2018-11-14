from flask import Flask, redirect, request, render_template, session
from tp_final.clases_tp_final.persona import Persona
from tp_final.clases_tp_final.pelicula import Pelicula
from tp_final.clases_tp_final.cine import Cine
from tp_final.clases_tp_final.horario import Horario
from tp_final.clases_tp_final.sala import Sala
from tp_final.clases_tp_final.butaca import Butaca
from tp_final.clases_tp_final.reserva import Reserva

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

contraseña_admin = "POLI"

def Session():
    if not 'dni' in session:
        session['dni'] = session.get('dni')

@app.route('/')
def Menu():
   return render_template('menu.html')

@app.route('/MenuAdmin')
def MenuAdmin():
    return render_template('MenuAdmin.html')

@app.route('/MostrarPelis')
def MostrarPelis():
    lista_pelis = Pelicula.ListarPeliculas()
    return render_template('MostrarPelis.html', lista_pelis=lista_pelis)

@app.route('/DarDeAltaPeli')
def DarDeAltaPeli():
    return render_template('/DarDeAltaPeli.html')

@app.route('/DarDeAltaPeliAction',methods = ['POST','GET'])
def DarDeAltaPeliAction():
    P = Pelicula
    P.nombre = request.form.get("nombre")
    P.genero = request.form.get("genero")
    P.estrellas = request.form.get("estrellas")
    P.Dar_de_Alta_Pelicula()
    return redirect('/MenuAdmin')

@app.route('/DarDeBajaPeli',methods = ['POST','GET'])
def DarDeBajaPeli():
    lista_pelis = Pelicula.ListarPeliculas()
    return render_template('/DarDeBajaPeli.html',lista_pelis=lista_pelis)

@app.route('/DarDeBajaPeliAction',methods = ['POST','GET'])
def DarDeBajaPeliAction():
    idpeli = request.form.get("pelicula")
    Pelicula.Dar_de_Baja_Pelicula(idpeli)
    return redirect('/MenuAdmin')


@app.route('/login_admin')
def login_admin():
    return render_template('login_admin.html')

@app.route('/loginAdminAction',methods = ['POST', 'GET'])
def loginAdminAction():
    contraseña = request.form.get("contraseña_admin")
    if contraseña == contraseña_admin:
        session["dni"] = request.form.get("dni")
        return redirect('/MenuAdmin')
    else:
        return redirect('/login_admin')

@app.route('/registroAdmin')
def registroAdmin():
    return render_template("registroAdmin.html")

@app.route('/registroAdminAction',methods = ['POST', 'GET'])
def registroAdminAction():
    p = Persona()
    p.nombre = request.form.get('nombre')
    p.apellido = request.form.get('apellido')
    p.contraseña = contraseña_admin
    p.Dar_de_Alta_Persona()
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/loginAction',methods = ['POST', 'GET'])
def loginAction():
    contraseña = request.form.get("contraseña")
    i = request.form.get("dni")
    p = Persona.ObtenerDatosPersona(i)
    if contraseña == p.contraseña:
        session["dni"] = request.form.get("dni")
        return redirect('/')
    else:
        return redirect('/login')

@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/signupAction',methods = ['POST', 'GET'])
def signupAction():
    p = Persona()
    p.nombre = request.form.get('nombre')
    p.apellido = request.form.get('apellido')
    p.contraseña = request.form.get('contraseña')
    p.Dar_de_Alta_Persona()
    return redirect('/')

@app.route('/Cerrar_Sesion')
def Cerrar_Serion():
    session.pop('dni',None)
    return redirect('/')

@app.route('/Pelis')
def Pelis():
    if "dni" in session:
        dni = session["dni"]
        p = Persona.ObtenerDatosPersona(dni)
        lista_peliculas = Pelicula.ListarPeliculas()
        lista_cines = Cine.ListarCines()
        return render_template('pelis.html', p=p, lista_peliculas=lista_peliculas, lista_cines=lista_cines)
    else:
        return redirect('/')

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
    if "dni" in session:
        dni = session['dni']
        Pe = Persona.ObtenerDatosPersona(dni)
        lista_reservas = Reserva.ListarReservas(dni)
        return render_template('ver_reservas.html', Pe=Pe, lista_reservas=lista_reservas)
    else:
        return redirect('/')

if __name__ == '__main__':
    app.run(debug = True)



# 1. RESERVA DE ENTRADA - GUARDAR EN db LA RESERVA (MOSTRAR SOLO LAS BUTACAS LIBRES)
# 3. ADMINISTRACION PARA AGREGAR MODIFICAR ELIMINAR PELICULAS

