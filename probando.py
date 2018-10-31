from pelicula import Pelicula

id = 1
p = Pelicula.InfoPeli(id)
lista = []
lista.append(p.nombre)
"""
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


def HorarioEnReserva(self):
    cursorHorarioEnReserva = DB.run(
        "Select * from Horarios join Reserva on Horarios.idHorarios = Reserva.Horarios_idHorarios where Reserva.idReserva = " + str(
            self.idReserva) + ";")
    H = Horario()
    for item in cursorHorarioEnReserva:
        H.idHorario = item['idHorarios']
        H.fecha_hora = item['fecha_hora']
        H.Sala_idSala = item['Sala_idSala']
        H.Pelicula_idPelicula = item['Pelicula_idPelicula']
        H.Cine_idCine = item['Cine_idCine']
    return H

<p><a href = "/registroAdmin"> <input type = "submit" value = "Iniciar Sesion como Administrador" ></a></p>
"""