from db import DB

class Butaca(object):
    idButaca = None
    id_sala = None
    precio_butaca = None

    def Dar_de_Alta_Butaca(self):
        DB.run("Insert into Butaca(idButaca,Sala_idSala,precio_butaca) VALUES (" + str(self.idButaca) + "," + str(self.id_sala) +"," + str(self.precio_butaca) +")")

    @staticmethod
    def get_butaca(idButaca):
        cursor_butaca = DB.run("Select * from Butaca where idButaca = "+idButaca+"")
        B = Butaca()
        dict = cursor_butaca.fetchone()
        B.idButaca = dict['idButaca']
        B.id_sala = dict['Sala_idSala']
        B.precio_butaca = dict['precio_butaca']
        return B
