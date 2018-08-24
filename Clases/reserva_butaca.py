from Clases.db import DB

class Reserva_Butaca(object):
    Reserva_idReserva = None
    Reserva_Cliente_dni = None
    Butaca_idButaca = None

    def Dar_de_Alta_Reserva_Butaca(self):
        DB.run("Insert into Reserva_Butaca(Reserva_idReserva,Reserva_Cliente_dni,BUtaca_idButaca) VALUES("+ str(self.Reserva_idReserva) +","+ str(self.Reserva_Cliente_dni) +","+ str(self.Butaca_idButaca) +");")