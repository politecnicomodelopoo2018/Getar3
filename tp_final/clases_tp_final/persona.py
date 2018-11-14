from tp_final.clases_tp_final.db import DB

class Persona(object):
    dni = None
    nombre = None
    apellido = None
    contraseña = None


    def Dar_de_Alta_Persona(self):
        cur = DB.run("Insert into Cliente(dni,nombre,apellido,contraseña) VALUES("'NULL'", '" + str(self.nombre) + "', '" + str(self.apellido) + "', '" + self.contraseña +"');")
        self.dni = cur.lastrowid

    @staticmethod
    def ObtenerDatosPersona(dni):
        cursorPersona = DB.run("Select * from Cliente where dni = " + str(dni)+";")
        P = Persona()
        for item in cursorPersona:
            P.dni = item['dni']
            P.nombre = item['nombre']
            P.apellido = item['apellido']
            P.contraseña = item['contraseña']
        return P

