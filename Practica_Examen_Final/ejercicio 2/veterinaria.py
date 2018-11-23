import datetime
from Practica_Examen_Final.ejercicio2.mascota import Perro
from Practica_Examen_Final.ejercicio2.mascota import Gato
from Practica_Examen_Final.ejercicio2.mascota import Tortuga

class Veterinaria(object):

    def __init__(self):
        self.lista_mascotas = []

    def AgregarMascota(self,M):
        self.lista_mascotas.append(M)

    def RazasDePerroQueNoCumplen(self):
        lista_razas = []
        for item in self.lista_mascotas:
            if type(item) == Perro:
                if item.MascotaCumpleConVisitas(datetime.today().year) == False:
                    if item.raza not in lista_razas:
                        lista_razas.append(item.raza)
        return lista_razas

    def TipiMascotaMejorAsistencia(self):
        lista_perros = []
        lista_gatos = []
        lista_tortugas = []
        for item in self.lista_mascotas:
            if item.MascotaCumpleConVisitas(datetime.today().year) == True:
                if type(item) == Perro:
                    lista_perros.append(item)
                if type(item) == Gato:
                    lista_gatos.append(item)
                if type(item) == Tortuga:
                    lista_tortugas.append(item)
        if lista_perros.length > lista_gatos.length and lista_perros.lenght > lista_tortugas.lenght:
            return "Perro"
        if lista_perros.length < lista_gatos.length and lista_gatos.lenght > lista_tortugas.lenght:
            return "Gato"
        if lista_tortugas.length > lista_gatos.length and lista_perros.lenght < lista_tortugas.lenght:
            return "Tortuga"