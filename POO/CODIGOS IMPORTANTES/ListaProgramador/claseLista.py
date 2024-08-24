import csv
from claseNodo import nodo
from claseObjeto import objeto       #Importar objetos

class lista:
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
            dato = self.__actual.getObjeto()
            self.__actual = self.__actual.getSiguiente()
            return dato
        
    def agregarFinal(self, objeto):
        nodo1 = nodo(objeto)
        if self.__comienzo == None:
            nodo1.setSiguiente(self.__comienzo)
            self.__comienzo = nodo1
            self.__actual = nodo1
            self.__tope += 1
        else:
            anterior = None
            actual =self.__comienzo
            while actual:
                anterior=actual
                actual=actual.getSiguiente()
            nodo1.setSiguiente(actual)
            anterior.setSiguiente(nodo1)
            self.__tope += 1

    def carga(self):        #Carga con archivo csv
        archivo=open("C:\\Users\\admin\\Desktop\\facuu\\2do año\\codigos\\Unidad 3\\PARCIAL MIO\\transporte.csv")
        leer=csv.reader(archivo,delimiter=';')
        next(leer)
        for fila in leer:
            o=objeto(fila[0], fila[1], fila[2], fila[3], float(fila[4]), precio=float(fila[5]), peso=float(fila[6]), cantidad=int(fila[7]), direccion=fila[8])
            self.agregarFinal(o)
        archivo.close()

    def ordenar(self):      #Ordenamiento con sobrecarga de operadores
        if self.__comienzo is None or self.__comienzo.getSiguiente() is None:
            return
        actual = self.__comienzo
        while actual.getSiguiente() is not None:
            siguiente = actual.getSiguiente()
            while siguiente is not None:
                if isinstance(actual.getObjeto(), objeto) and isinstance(siguiente.getObjeto(), objeto):     #Si en la lista hay objetos de clases diferentes
                    if actual.getObjeto() > siguiente.getObjeto():
                        aux = actual.getObjeto()
                        actual.setObjeto(siguiente.getObjeto())
                        siguiente.setObjeto(aux)
                siguiente = siguiente.getSiguiente()
            actual = actual.getSiguiente()

    def mostrar(self):      #Mostrar desde el gestor
        self.ordenar()
        x=0
        aux=self.__comienzo
        print("Contratante          Costo total\n")
        while aux is not None:
            if isinstance(aux.getObjeto(), objeto):      #Si en la lista hay objetos de clases diferentes
                print(f"{aux.getObjeto().getNomCont()}             {aux.getObjeto().costoTotal()}\n")
                x+=aux.getObjeto().costoTotal()
            aux=aux.getSiguiente()
        print(f"Total: {x}")

    def mostrar(self):      #Mostrar con el meodo definido en la clase
        actual=self.__comienzo
        while actual:
            print(actual.getEquipo().mostrar())
            actual = actual.getSiguiente()

    def cantidad(self):
        cont=0
        aux=self.__comienzo
        while aux!= None:
            if isinstance(aux.getObjeto(), objeto) and aux.getObjeto().getPeso()>50:  #Si en la lista hay objetos de clases diferentes
                cont+=1
            aux=aux.getSiguiente()
        print(f"La cantidad de Objetos de embalaje que superan los 50kg son: {cont}\n")

    def fecha(self):
        xfecha=input("Ingrese una fecha\n")
        aux=self.__comienzo
        cont1=0
        cont2=0
        while aux!=None:
            if aux.getObjeto().getFecha() == xfecha: 
                if isinstance(aux.getObjeto(), objeto):  #Si en la lista hay objetos de clases diferentes
                    cont1 +=1
                else:
                    cont2 +=1
            aux = aux.getSiguiente()
        if cont1 > cont2:
            print("El Objeto Mas contratado fue el de Transporte")
        else:
            print("El Objeto mas contratado fue el de Embalaje")

    def longitud(self):
        cant=0
        aux=self.__comienzo
        while aux!=None:
            cant+=1
            aux=aux.getSiguiente()
        return cant
    
    def pos(self):      #Busqueda por posicion
        cant=self.longitud()
        i=int(input(f"La lista posee {cant} elementos, elegir un numero del 0 al {cant}: "))
        i=i-1
        if i<0 or i>cant-1:
            raise IndexError
        c=0
        aux=self.__comienzo
        while c!=i:
            aux=aux.getSiguiente()
            c+=1
        if(isinstance(aux.getObjeto(), objeto)):
            print(f"El equipo numero: {i+1} es maquinaria pesada\n")
        elif(isinstance(aux.getObjeto(), objeto)):
            print(f"El equipo numero: {i+1} es maquinaria electrica\n")
        else:
            print("tipo no reconocido\n")