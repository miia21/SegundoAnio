from claseEquipo import Equipo
import csv

class GestorEquipo:
    def __init__(self):
        self.__Equipo = []
    def cargaEquipo(self):
        with open('C:\\Users\\germi\\Desktop\\Ejercicio 5\\equipos2024.csv') as archi:
            leer = csv.reader(archi, delimiter = ';')
            next(leer)
            for raw in leer:
                eq = Equipo(raw[0],raw[1],raw[2],raw[3],raw[4],raw[5])
                self.__Equipo.append(eq)
    def mostrarEquipo(self):
        x = Equipo()
        for i in range(len(self.__Equipo)):
            self.__Equipo[i].mostrar()
    def buscarId(self,nombre):
        i = 0
        e = False
        while not e and i < len(self.__Equipo):
            if (nombre == self.__Equipo[i].getNombre()):
                e = True
                return self.__Equipo[i].getIdentificador()
            else:
                i += 1
        
    def buscar(self,gf):
        nomb = input("Ingresar nombre del equipo: ")
        id = self.buscarId(nomb)
        print(f"-----------------------------------------------------------------------------------------------------")
        print(f"Equipo: {nomb}")
        gf.Listar(id)
        
    def actualizar(self,gf):
        for id in range(len(self.__Equipo)):
            favor = gf.buscarFavor(id)
            contra = gf.buscarContra(id)
            diferencia = gf.buscarDiferencia(id)
            puntos = gf.buscarPuntos(id)
            self.__Equipo[id].setFavor(int(favor))
            self.__Equipo[id].setContra(int(contra))
            self.__Equipo[id].setDiferencia(int(diferencia))
            self.__Equipo[id].setPuntos(int(puntos))
    def ordenar (self):
        self.__Equipo.sort(reverse=True)
        for i in range(len(self.__Equipo)):
            self.__Equipo[i].mostrar()
    def almacenar(self):
        with open('nuevatabla.csv','w',newline='') as archi2:
            nuevo = csv.writer(archi2)
            nuevo.writerow(['ID','Nombre','A favor','En contra','Diferencia','Puntos'])
            for i in range(len(self.__Equipo)):
                nuevo.writerow([self.__Equipo[i].getIdentificador(), self.__Equipo[i].getNombre(),self.__Equipo[i].getFavor(),self.__Equipo[i].getContra(), self.__Equipo[i].getDiferencia(), self.__Equipo[i].getPuntos()])
        print("La tabla de posiciones ordenada se ha guardado con exito\n")