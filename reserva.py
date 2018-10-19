from db import DB

class Reserva(object):
    idReserva = None
    Cliente_dni = None
    Horarios_idHorario = None
    Horarios_Sala_idSala = None
    Pelicula_idPelicula = None

    def Dar_de_Alta_Reserva(self):
        DB.run("Insert into Reserva(idReserva, Cliente_dni, Horarios_idHorarios, Horarios_Sala_idSala ,Pelicula_idPelicula) VALUES("+ str(self.idReserva) +","+ str(self.Cliente_dni) +","+str(self.Horarios_idHorario)+","+ str(self.Horarios_Sala_idSala) +","+ str(self.Pelicula_idPelicula) +");")

