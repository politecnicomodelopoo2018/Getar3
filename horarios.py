from db import DB

class Horario(object):
    idHorario = None
    dia = None
    hora = None
    precio_butaca = None
    Sala_idSala = None
    Sala_Cine_idCine = None
    Pelicula_idPelicula = None

    def Dar_de_Alta_Horario(self):
        DB.run("Insert into Horario(idHorario,dia,hora,precio_butaca,Sala_idSala,Sala_Cine_idCine,Pelicula_idPelicula) VALUES(" + str(self.idHorario) + ", " + str(self.dia) + ","+ str(self.hora) +","+ str(self.precio_butaca) +"," + str(self.Sala_idSala) + ", " + str(self.Sala_Cine_idCine) + ");")