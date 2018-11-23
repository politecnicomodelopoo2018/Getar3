import datetime

class Mascota(object):
    nombre = None
    fecha_nacimiento = None
    dueño = None
    visistas_minimas = None

    def __init__(self):
        self.lista_visitas = []

    def MascotaCumpleConVisitas(self,año):
        lista_visitas_año_actual = []
        for item in self.lista_visitas:
            if item.datetime.date.year == año:
                lista_visitas_año_actual.append(item)
        if lista_visitas_año_actual.lenght() < self.visistas_minimas:
            return False

        return True

    def MascotasAsistenciaPerfecta(self):
        for item in range(self.fecha_nacimiento.year,datetime.today().year):
            if self.MascotaCumpleConVisitas(item) == False:
                return False
        return True

class Perro(Mascota):
    raza = None
    visitas_minimas = 4

class Gato(Mascota):
    raza = None
    visitas_minimas = 2

class Tortuga(Mascota):
    visitas_minimas = 1