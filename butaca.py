from db import DB

class Butaca(object):
    idButaca = None
    id_sala = None
    disponible = None

    def Dar_de_Alta_Butaca(self):
        DB.run("Insert into Butaca(idButaca,Sala_idSala) VALUES (" + str(self.idButaca) + "," + str(self.id_sala) +"," + str(self.disponible) +")")