from db import DB
from pelicula import Pelicula

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

    @staticmethod
    def PeliculaEnReserva(dni):
        cursorPeliEnReserva = DB.run("Select * from Pelicula where Reserva.Cliente_dni = "+str(dni)+";")
        Peli = Pelicula()
        for item in cursorPeliEnReserva:
            Peli.idPelicula = item['idPelicula']
            Peli.nombre = item['nombre']
            Peli.estrellas = item['estrellas']
            Peli.genero = item['genero']
        return Peli