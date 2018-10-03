from db import DB

class Sala(object):
    idSala = None

    def Dar_de_Alta_Sala(self):
        DB.run("Insert into Sala(idSala) Values (" + str(self.idSala) + ")")