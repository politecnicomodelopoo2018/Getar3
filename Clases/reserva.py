from Clases.db import DB

class Reserva(object):
    idReserva = None
    Cliente_dni = None
    Horarios_idHorario = None
    Horarios_Sala_idSala = None
    Horarios_Sala_Cine_idCine = None

    def Dar_de_Alta_Reserva(self):
        DB.run("Insert into Reserva(idReserva,Cliente_dni,Horarios_idHorario,Horarios_Sala_idSala,Horarios_Sala_Cine_idCine) VALUES("+ str(self.idReserva) +","+ str(self.Cliente_dni) +","+str(self.Horarios_idHorario)+","+ str(self.Horarios_Sala_idSala) +","+ str(self.Horarios_Sala_Cine_idCine) +");")

    def Dar_de_Baja_Reserva(self):
        DB.run("Delete from Reserva")