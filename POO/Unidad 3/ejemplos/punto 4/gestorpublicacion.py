from libro import *
from cd import *
from nodo import *
import csv
class gestor:
    __inicio=Nodo

    def __init__(self):
        self.__inicio=None

    def agregar(self,objeto):
        nodo = Nodo(self.__inicio,objeto)
        nodo.setSig(self.__inicio)
        self.__inicio=nodo

    def carga(self):
        archivo=open("cpp/practica 3/punto 4/publicaciones.csv")
        reader=csv.reader(archivo,delimiter=';')
        bandera=False
        for fila in reader:
            if bandera==False:
                bandera=True
            elif fila[3]=="L":
                titulo=fila[0]
                categoria=fila[1]
                preciobase=float(fila[2])
                autor=fila[4]
                edicion=fila[6]
                paginas=int(fila[5])
                libroo=libro(titulo,categoria,preciobase,autor,edicion,paginas)
                self.agregar(libroo)
            elif fila[3]=="A":
                titulo=fila[0]
                categoria=fila[1]
                preciobase=float(fila[2])
                duracion=fila[5]
                narrador=fila[4]
                audio=disco(titulo,categoria,preciobase,duracion,narrador)
                self.agregar(audio)
    
    def nuevo(self):
        op=int(input("""Ingrese:
                     1:Nuevo libro
                     2:Nuevo CD"""))
        if op==1:
                titulo=input("Ingrese Titulo:")
                categoria=input("Ingrese categoria:")
                preciobase=float(input("Ingrese precio base:"))
                autor=input("Ingrese autor:")
                edicion=input("Ingrese fecha de publicacion:")
                paginas=input("Ingrese numero de paginas:")
                libroo=libro(titulo,categoria,preciobase,autor,edicion,paginas)
                self.agregar(libroo)
        elif op==2:
                titulo=input("Ingrese titulo:")
                categoria=input("Ingrese categoria:")
                preciobase=float(input("Ingrese precio base:"))
                duracion=int(input("Ingrese duracion:"))
                narrador=input("Ingrese narrador:")
                audio=disco(titulo,categoria,preciobase,duracion,narrador)
                self.agregar(audio)

    def mostrartipo(self):
        lugar=int(input("Ingrese lugar en la lista"))
        i=0
        banda=False
        actual=self.__inicio
        while actual and banda==False:
            if i==lugar:
                datos=actual.getdatos()
                if isinstance(datos,libro):
                    banda=True
                    print("La clase de este lugar es de tipo libro")
                elif isinstance(datos,disco):
                    banda=True
                    print("La clase de este lugar es de tipo audiolibro")
            actual=actual.getSig()
            i+=1
    
    def contartipo(self):
        libros=0
        audios=0
        actual=self.__inicio
        while actual:
            datos=actual.getdatos()
            if isinstance(datos,libro):
                libros+=1
            if isinstance(datos,disco):
                audios+=1
            actual=actual.getSig()
        print(f"Hay en la lista {libros} libros y {audios} audiolibros")
    """"
    def mostrartodo(self):
        actual=self.__inicio
        while actual:
            print(self.__inicio)
            actual=actual.getSig()
        """ 
    def mostrartodo(self):
        actual=self.__inicio
        while actual:
           print(actual.getdatos())
           actual=actual.getSig()