from tp_final.clases_tp_final.db import DB
from tp_final.clases_tp_final.sala import Sala

class Horario(object):
    idHorario = None
    fecha_hora = None
    Sala_idSala = None
    Pelicula_idPelicula = None
    Cine_idCine = None

    def Dar_de_Alta_Horario(self):
        DB.run("Insert into Horarios(idHorarios,fecha_hora,Sala_idSala,Pelicula_idPelicula,Cine_idCine) VALUES(" + str(self.idHorario) + ",'"+ (self.fecha_hora) +"'," + str(self.Sala_idSala) + ","+ str(self.Pelicula_idPelicula) +", " + str(self.Cine_idCine) + ");")

    @staticmethod
    def GetInfoHorarios(idHorario):
        cursorInfoHorario = DB.run("Select * from Horarios where idHorarios = '" + idHorario + "';")
        H = Horario()
        for item in cursorInfoHorario:
            H.idHorario = item["idHorarios"]
            H.fecha_hora = item["fecha_hora"]
            H.Sala_idSala = item["Sala_idSala"]
            H.Pelicula_idPelicula = item["Pelicula_idPelicula"]
            H.Cine_idCine = item["Cine_idCine"]
        return H

    @staticmethod
    def GetSala_En_Horario(idHorario):
        cursorSala_En_Horario = DB.run("Select * from Sala join Horarios on Horarios.Sala_idSala = Sala.idSala where Horarios.idHorarios = '" + idHorario + "';")
        S = Sala()
        for item in cursorSala_En_Horario:
            S.idSala = item['idSala']
        return S
