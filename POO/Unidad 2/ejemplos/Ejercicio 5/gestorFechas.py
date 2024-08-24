from claseFechas import Fecha
import csv

class GestorFechas:
    def __init__(self):
        self.__Fechas = []
    def cargaFechas(self):
        with open('C:\\Users\\germi\\Desktop\\Ejercicio 5\\FechasFutbol.csv') as archi:
            leer = csv.reader(archi,delimiter=';')
            next(leer)
            for raw in leer:
                fe = Fecha(raw[0],raw[1],raw[2],raw[3],raw[4])
                self.__Fechas.append(fe)
    def mostrarFechas(self):
        for i in range(len(self.__Fechas)):
            self.__Fechas[i].mostrar()
    def Listar(self,id):
        i = 0
        diferencia = 0
        favor = 0
        contra = 0
        puntos = 0
        acum = 0
        print("Fecha        Goles a Favor      Goles en Contra      Diferencia de Goles          Puntos")
        for i in range(len(self.__Fechas)):
            if id == self.__Fechas[i].getIdLocal():
                diferencia += self.__Fechas[i].getGolesLocal() - self.__Fechas[i].getGolesVisitante()
                favor += self.__Fechas[i].getGolesLocal()
                contra += self.__Fechas[i].getGolesVisitante()
                if (self.__Fechas[i].getGolesLocal() > self.__Fechas[i].getGolesVisitante()):
                    puntos += 3
                    acum += 3
                elif (self.__Fechas[i].getGolesLocal() == self.__Fechas[i].getGolesVisitante()):
                    puntos += 1
                    acum += 1
                print(f"{self.__Fechas[i].getFecha()}         {self.__Fechas[i].getGolesLocal()}                   {self.__Fechas[i].getGolesVisitante()}                        {self.__Fechas[i].getGolesLocal() - self.__Fechas[i].getGolesVisitante()}                   {puntos}")
            elif id == self.__Fechas[i].getIdVisitante():
                diferencia += self.__Fechas[i].getGolesVisitante() - self.__Fechas[i].getGolesLocal()
                favor += self.__Fechas[i].getGolesVisitante()
                contra += self.__Fechas[i].getGolesLocal()
                if (self.__Fechas[i].getGolesVisitante() > self.__Fechas[i].getGolesLocal()):
                    puntos += 3
                    acum += 3
                elif (self.__Fechas[i].getGolesVisitante() == self.__Fechas[i].getGolesLocal()):
                    puntos += 1
                    acum += 1
                print(f"{self.__Fechas[i].getFecha()}         {self.__Fechas[i].getGolesVisitante()}                   {self.__Fechas[i].getGolesLocal()}                        {self.__Fechas[i].getGolesVisitante() - self.__Fechas[i].getGolesLocal()}                   {puntos}")
        print("--------------------------------------------------------------------------------------------------------------")
        print(f"Totales:           {favor}                   {contra}                        {diferencia}                   {acum}")
  
    def buscarFavor(self,id):
        favor = 0
        for i in range(len(self.__Fechas)):
            if (id == self.__Fechas[i].getIdLocal()):
                favor += self.__Fechas[i].getGolesLocal()
            elif (id == self.__Fechas[i].getIdVisitante()):
                favor += self.__fechas[i].getGolesVisitante()
        return favor
    def buscarContra(self,id):
        contra = 0
        for i in range(len(self.__Fechas)):
            if id == self.__Fechas[i].getIdLocal():
                contra += self.__Fechas[i].getGolesVisitante()
            elif id == self.__Fechas[i].getIdVisitante():
                contra += self.__Fechas[i].getGolesLocal()
        return contra
    def buscarDiferencia(self,id):
        diferencia = 0
        for i in range(len(self.__Fechas)):
            if (id == self.__Fechas[i].getIdLocal()):
                diferencia += self.__Fechas[i].getGolesLocal() - self.__Fechas[i].getGolesVisitante()
            elif (id == self.__Fechas[i].getIdVisitante()):
                diferencia += self.__Fechas[i].getGolesVisitante() - self.__Fechas[i].getGolesLocal()
        return diferencia
    def buscarPuntos(self, id):
        puntos = 0
        for i in range(len(self.__Fechas)):
            if (id == self.__Fechas[i].getIdLocal()):
                if (self.__Fechas[i].getGolesLocal() > self.__Fechas[i].getGolesVisitante()):
                    puntos += 3
                elif (self.__Fechas[i].getGolesLocal() == self.__Fechas[i].getGolesVisitante()):
                    puntos += 1
            elif (id == self.__Fechas[i].getIdVisitante()):
                if (self.__Fechas[i].getGolesVisitante() > self.__Fechas[i].getGolesLocal()):
                    puntos += 3
                elif (self.__Fechas[i].getGolesVisitante() == self.__Fechas[i].getGolesLocal()):
                    puntos += 1
        return puntos
