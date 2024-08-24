import csv
from claseNodo import nodo
from clasePlanes import Planes
from claseTelefonia import Telefonia
from claseTelevision import Television

class Lista:
    __comienzo: nodo
    __actual : nodo
    __tope : int
    __indice : int
    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__tope = 0
        self.__indice = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice +=1
            dato = self.__actual.getPlanes()
            self.__actual = self.__actual.getSiguiente()
            return dato
    def carga(self):
        with open('C:\\Users\\germi\\Desktop\\Practica\\Practica\\planes.csv') as archi:
            leer = csv.reader(archi, delimiter=';')
            next(leer)
            for fila in leer:
                if fila[0] == 'M':
                    telefonia = Telefonia(fila[1], fila[2], fila[3], fila[4], tipoLlamada=fila[5], cantMinutos=fila[6])
                    unnodo = nodo(telefonia)
                elif fila[0] == 'T':
                    television = Television(fila[1], fila[2], fila[3], fila[4], nacionales=fila[5], internacionales=fila[6])
                    unnodo = nodo(television)
                if self.__comienzo is None:
                    self.__comienzo = unnodo
                else:
                    aux = self.__comienzo
                    while aux.getSiguiente() is not None:
                        aux = aux.getSiguiente()
                    aux.setSiguiente(unnodo)
        archi.close()
     
    def longitud(self):
        cant=0
        aux = self.__comienzo
        while aux!= None:
            cant+=1
            aux = aux.getSiguiente()
        return cant
    def pos(self):
        cant = self.longitud()
        i=int(input(f"Ingresar un numero de indice para ver el tipo de plan\n"))
        i=i-1
        if i<0 or i>cant-1:
            raise IndexError
        c=0
        aux= self.__comienzo
        while c!=i:
            aux=aux.getSiguiente()
            c+=1
        if(isinstance(aux.getPlanes(),Telefonia)):
            print(f"El plan es Telefonico")
        elif (isinstance(aux.getPlanes(),Television)):
            print(f"El plan es de television")
        else:
            print("Error")
    def contador(self):
        cob =input("Ingresar la cobertura geografica: ")
        try:
            cob = str(cob)
        except ValueError:
            print("Error, No ingresar numeros")
        else:
            aux = self.__comienzo
            cant = 0
            while aux != None:
                if cob.lower() in aux.getPlanes().getCobertura():
                    cant +=1
                aux = aux.getSiguiente()
            print(f"La cobertura {cob} tiene {cant} cantidad de planes")
    def canales(self):
        canales = int(input("Ingresar una cantidad de canales internacionales: "))
        try:
            canales = int(canales)
        except ValueError:
            print("Ingresar un numero valido")
        else:
            aux = self.__comienzo
            flag = False
            while aux is not None:
                if isinstance(aux.getPlanes(),Television) and canales <= aux.getPlanes().getInternacionales():
                    print(f"{aux.getPlanes().getNomb()}\n")
                    flag = True
                aux = aux.getSiguiente()
            if flag is False:
                print("No existen canales con esa cantidad")
            
    def mostrar(self):
        aux=self.__comienzo
        while aux is not None:
            if isinstance(aux.getPlanes(), Telefonia):
                print(f"Telefonia")
                aux.getPlanes().mostrar()
            elif isinstance(aux.getPlanes(),Television):
                print(f"Television ")
                aux.getPlanes().mostrar()
            aux=aux.getSiguiente()