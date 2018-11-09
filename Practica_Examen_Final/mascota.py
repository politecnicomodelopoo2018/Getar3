class Mascota(object):
    nombre = None
    saludo = None
    alegria = 1
    dueño = None

    def Saludar(self,persona):
        if self.dueño == persona:
            if self.alegria > 1:
                for item in range(self.alegria):
                    return self.saludo
                self.alegria = self.alegria - 1
            else:
                return self.saludo
        else:
            return self.saludo.upper()+"!"

    def __init__(self,nombre,dueño):
        self.nombre = nombre
        self.dueño = dueño



class Perro(Mascota):
    saludo = "guau"
