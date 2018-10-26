from db import DB
from pelicula import Pelicula
from horario import Horario
from butaca import Butaca

class Reserva(object):
    idReserva = None
    Cliente_dni = None
    Horarios_idHorario = None
    Horarios_Sala_idSala = None
    Pelicula_idPelicula = None

    def Dar_de_Alta_Reserva(self):
        DB.run("Insert into Reserva(idReserva, Cliente_dni, Horarios_idHorarios, Horarios_Sala_idSala ,Pelicula_idPelicula) VALUES("+ str(self.idReserva) +","+ str(self.Cliente_dni) +","+str(self.Horarios_idHorario)+","+ str(self.Horarios_Sala_idSala) +","+ str(self.Pelicula_idPelicula) +");")

    @staticmethod
    def ListarReservas(dni):
        cursorReservas = DB().run("Select * from Reserva where Reserva.Cliente_dni = "+str(dni)+";")
        ListaReservas = []
        for item in cursorReservas:
            R = Reserva()
            R.idReserva = item["idReserva"]
            R.Cliente_dni = item["Cliente_dni"]
            R.Horarios_idHorario = item["Horarios_idHorarios"]
            R.Horarios_Sala_idSala = item["Horarios_Sala_idSala"]
            R.Pelicula_idPelicula = item["Pelicula_idPelicula"]
            ListaReservas.append(R)
        return ListaReservas


    def PeliculaEnReserva(self):
        cursorPeliEnReserva = DB.run("Select * from Pelicula join Reserva on Pelicula.idPelicula = Reserva.Pelicula_idPelicula where Reserva.idReserva = "+str(self.idReserva)+";")
        Peli = Pelicula()
        for item in cursorPeliEnReserva:
            Peli.idPelicula = item['idPelicula']
            Peli.nombre = item['nombre']
            Peli.estrellas = item['estrellas']
            Peli.genero = item['genero']
        return Peli


    def HorarioEnReserva(self):
        cursorHorarioEnReserva = DB.run("Select * from Horarios join Reserva on Horarios.idHorarios = Reserva.Horarios_idHorarios where Reserva.idReserva = " + str(self.idReserva) + ";")
        H = Horario()
        for item in cursorHorarioEnReserva:
            H.idHorario = item['idHorarios']
            H.fecha_hora = item['fecha_hora']
            H.Sala_idSala = item['Sala_idSala']
            H.Pelicula_idPelicula = item['Pelicula_idPelicula']
            H.Cine_idCine = item['Cine_idCine']
        return H

    def ButacaEnReserva(self):
        cursorButacaEnReserva = DB.run("Select * from Butaca join Reserva on Reserva.Horarios_Sala_idSala = Butaca.Sala_idSala where Reserva.idReserva = " + str(self.idReserva) + ";")
        B = Butaca()
        for item in cursorButacaEnReserva:
            B.idButaca = item['idButaca']
            B.id_sala = item['Sala_idSala']
            B.precio_butaca = item['precio_butaca']
        return B

