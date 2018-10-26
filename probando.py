from pelicula import Pelicula

id = 1
p = Pelicula.InfoPeli(id)
lista = []
lista.append(p.nombre)


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