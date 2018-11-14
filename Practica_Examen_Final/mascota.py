from Practica_Examen_Final.sistema import Sistema

s = Sistema()

class Mascota(object):
    idm = None
    nombre = None
    saludo = None
    alegria = 1
    dueño = None

    def __init__(self,idm,nombre,dueño):
        self.idm = idm
        self.nombre = nombre
        self.dueño = dueño

    def Saludar(self,persona):
        if self.dueño == persona:
            if self.alegria > 1:
                for item in range(self.alegria):
                    return self.saludo + " "
                self.alegria = self.alegria - 1
            else:
                return self.saludo
        else:
            return self.saludo.upper()+"!"

    def Alimentar(self):
        return self.alegria + 1

class Perro(Mascota):
    saludo = "guau"

    pass

class Gato(Mascota):
    saludo = "miau"

    pass

class Pez(Mascota):
    alegria = 10
    muerte = None
    saludo = None

    def Saludar(self,persona):
        if self.dueño == persona:
            self.alegria = self.alegria - 1
            if self.alegria == 0:
                self.muerte = True
                s.lista_animales.remove()
            else:
                pass
        else:
            self.alegria = 0
            self.muerte = True
            s.lista_animales.remove()