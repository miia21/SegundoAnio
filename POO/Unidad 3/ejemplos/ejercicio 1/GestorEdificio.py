from claseEdificio import Edificio
import csv
from claseDepartamento import departemento
class GestorE:
    __ListaEdificio : list
    def __init__(self):
        self.__ListaEdificio = []
    def CargaArchivo (self):
        aux = 0
        archivo = open("EdificioNorte.csv")
        reader = csv.reader (archivo,delimiter=";")
        for fila in reader:
            if aux != fila[0]:
                aux = fila[0]
                edifi = Edificio(int(fila[0]),fila[1],fila[2],fila[3],int(fila[4]),int(fila[5]))
                self.__ListaEdificio.append(edifi)
                #Identificador/Nombre/Direccio/NombreEmpresa/CantidadPisos/CantidadDepartamento
                #self.Añadir(Edificio(int(fila[0]),fila[1],fila[2],fila[3],int(fila[4]),int(fila[5])))
            else:
                 #identificaion/NOMBRE y APELLIDO/NUMERO DE PISOS/NUMERO DE DEPARTAMENTO/CANTIDAD HABITACION/CANTIDAD BAÑOS/SUPERFICIE
                 #se pone aux - 1 porque la carga de lista tiene que empezar con 0 y como antes tenemos un edificio entonces el aux empieza en 1
                self.__ListaEdificio[int(aux)-1].setDepa(int(fila[1]),fila[2],int(fila[3]),int(fila[4]),int(fila[5]),int(fila[6]),float(fila[7]))

    def Mostrar (self):
        long = len(self.__ListaEdificio)
        for i in range(long):
            print("",self.__ListaEdificio[i].getNombre())
            self.__ListaEdificio[i].mostrarDepartamento()
        print("-----------------------------------------------------------------------------------")

    def BuscarPropied (self,nombre):
        #long = len(self.__ListaEdificio)
        i = 0
        ban = False
        while i < len(self.__ListaEdificio) and ban!=True:
            if nombre == self.__ListaEdificio[i].getNombre():
                ban = True
                print("Cambio la bandera")
                self.__ListaEdificio[i].MostrarInquilinos()
            else:
                print("Incremento el i")
                i+=1
        assert ban is True
        print("-------------------------------------------------------------------------------------")

    def SupEdifi (self,nom):
        ban = False
        i=0
        while i < len(self.__ListaEdificio) and ban != True:
            if nom == self.__ListaEdificio[i].getNombre():
                dat = self.__ListaEdificio[i].calcular()
                print("La superficio total del edifcio es : ",dat)
                ban = True
            else:
                i+=1
        assert ban is True,"Erro. No existe un edificion con ese nombre"
        print("-------------------------------------------------------------------------------------")
        
    def SuperPropie (self,nom):
        i=0
        ban = False
        while i<len(self.__ListaEdificio) and ban != True:
            condi = self.__ListaEdificio[i].BuscraPro(nom)
            if condi == True:
                print("Bandera verdadera")
                ban = True
                sup = self.__ListaEdificio[i].calcular()
                print("la superficie es : ",sup)
                sup2 = self.__ListaEdificio[i].SupPropi(nom)
                print("la superficie del propietario es : ",sup2)
                print("El porcentaje de la supeficie del propietario en el edificio es : %",(100*sup2)/sup)
            else:
                i+=1
        print("---------------------------------------------------------------------------------------")
    
    def MostraCanti(self,num):
        for i in range(len(self.__ListaEdificio)):
            cont = 0
            cont += self.__ListaEdificio[i].MostrarPiso(num)
            print("El edificio : ",self.__ListaEdificio[i].getNombre())
            print("La cantidad de departamentos con esas condiciones son : ",cont)
        print("----------------------------------------------------------------------------------------")
        

