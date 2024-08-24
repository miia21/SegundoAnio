from nodo import nodo
from ClaseLibro import Libro
from ClaseAudiolibro import audiolibro
import csv
class lista:
    __comienzo: nodo
    def __init__(self):
        self.__comienzo=None
    def carga(self):
        archivo=open("G:\\Otros ordenadores\\Mi portátil\\POO\\U3\\EJ4\\libros.csv")
        leer=csv.reader(archivo,delimiter=';')
        next(leer)
        for fila in leer:
            unlibro=Libro(fila[0],fila[1],float(fila[2]),fila[3],fila[4],int(fila[5]))
            unnodo=nodo(unlibro)
            unnodo.setSiguiente(self.__comienzo)
            self.__comienzo=unnodo
        archivo.close()
        libro=unnodo.getpublicacion()
        nomb=libro.gettitulo()
        print(f"libros cargados, ultimo libro: {nomb}")
        archivo=open("G:\\Otros ordenadores\\Mi portátil\\POO\\U3\\EJ4\\cd.csv")
        leer=csv.reader(archivo,delimiter=';')
        next(leer)
        for fila in leer:
            unaudiolibro=audiolibro(fila[0],fila[1],float(fila[2]),fila[3],fila[4])
            unnodo=nodo(unaudiolibro)
            unnodo.setSiguiente(self.__comienzo)
            self.__comienzo=unnodo
        archivo.close()
        audio=unnodo.getpublicacion()
        nomb=audio.gettitulo()
        print(f"audiolibros cargados, ultimo audiolibro: {nomb}")
    def agregar(self):
        c=0
        while c!=3:
            print("-------------------------------------------------------------")
            c=int(input("Ingresar una opcion: (1.Audiolibro 2.Libro 3.salir): "))
        
            if c==1:
                titulo=input("ingresar el titulo de la publicacion: ")
                categoria=input("ingresar la categoria: ")
                precio=float(input("ingresar el precio: "))
                nomb=input("ingresar nombre del narrador: ")
                duracion=int(input("ingresar duracion: "))
                unaudiolibro=audiolibro(titulo,categoria,precio,nomb,duracion)
                unnodo=nodo(unaudiolibro)
                unnodo.setSiguiente(self.__comienzo)
                self.__comienzo=unnodo
            elif c==2:
                titulo=input("ingresar el titulo de la publicacion: ")
                categoria=input("ingresar la categoria: ")
                precio=float(input("ingresar el precio: "))
                nombrea=input("ingresar el nombre del autor: ")
                fecha=input("ingresar fecha de publicacion: ")
                cantpags=input("ingresar cantidad de paginas")
                unlibro=Libro(titulo,categoria,precio,nombrea,fecha,cantpags)
                nod=nodo(unlibro)
                nod.setSiguiente(self.__comienzo)
                self.__comienzo=nod
    def longitud(self):
        cant=0
        aux=self.__comienzo
        while aux!=None:
            cant+=1
            aux=aux.getSiguiente()
        return cant
    def mostrarclase(self):
        print("--------------------------------------------")
        cant=self.longitud()
        i=int(input(f"La lista posee {cant} elementos, elegir un numero del 0 al {cant}: "))
        i=i-1
        c=0
        aux=self.__comienzo
        while c!=i:
            aux=aux.getSiguiente()
            c+=1
        if(isinstance(aux.getpublicacion(),Libro)):
            print(f"La publicacion numero: {i+1} es un Libro")
        elif(isinstance(aux.getpublicacion(),audiolibro)):
            print(f"La publicacion numero: {i+1} es un Audio Libro")
        else:
            print("tipo no reconocido")
    def muestracant(self):
        aux=self.__comienzo
        cA=0
        cL=0
        while aux!=None:
            P=aux.getpublicacion()
            if isinstance(P,Libro):
                cL+=1
            elif isinstance(P,audiolibro):
                cA+=1
            aux=aux.getSiguiente()
        print("------------------------------------------------------------------------------------------------")
        print(f"La cantidad de Libros publicados es de: {cL}\nLa cantidad de Audio Libros publicados es de: {cA}")
    def muestradatos(self):
        aux=self.__comienzo
        print("----------------------------------------------------------------------")
        while (aux!= None):
            P=aux.getpublicacion()
            if isinstance(P,Libro):
                importe=P.importetotal()
                print(f"Libro: {P.gettitulo()}\nCategoria: {P.getcategoria()}\n Importe: {importe*-1: .02f}")
            elif isinstance(P,audiolibro):
                precio=P.getprecio()
                importe=(precio * 1.10)
                print(f"Libro: {P.gettitulo()}\nCategoria: {P.getcategoria()}\n Importe: {(importe): .02f}")
            aux=aux.getSiguiente()