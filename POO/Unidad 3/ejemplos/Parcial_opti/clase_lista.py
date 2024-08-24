from clase_s_embalaje import Embalaje
from clase_s_transporte import Transporte
from clase_nodo import Nodo

class Lista():
    __comienzo : Nodo
    __actual : Nodo
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
            dato = self.__actual.objeto
            self.__actual = self.__actual.siguiente
            return dato
    def agregar_al_final(self,objeto):
        nodo = Nodo(objeto)
        if self.__comienzo == None:
            nodo.siguiente = self.__comienzo
            self.__comienzo = nodo
            self.__actual = nodo
            self.__tope += 1
        else:
            anterior = None
            actual =self.__comienzo
            while actual:
                anterior=actual
                actual=actual.siguiente
            nodo.siguiente = actual
            anterior.siguiente=nodo
            self.__tope += 1
    def inciso_1(self):
        op=int(input("Ingrese Opcion\n[1] Agregar Servicio de Transporte\n[2] Agregar Servicio de Embalaje\n"))
        if op==1:
            a=input("Ingrese Nombre de Empresa:")
            b=input("Ingrese Nombre de Contratante:")
            c=input("Ingrese Direccion:")
            d=input("Ingrese Fecha:")
            e=float(input("Ingrese Comision:"))
            f=float(input("Ingrese Precio Por hora del servicio:"))
            g=float(input("Ingrese Peso de la Carga:"))
            h=input("Ingrese direccion del destinto")
            i=int(input("Ingrese cantidad de horas del servicio"))
            objeto = Transporte(a,b,c,d,e,f,g,h,i)
            self.agregar_al_final(objeto)
        elif op==2:
            a=input("Ingrese Nombre de Empresa:")
            b=input("Ingrese Nombre de Contratante:")
            c=input("Ingrese Direccion:")
            d=input("Ingrese Fecha:")
            e=float(input("Ingrese Comision:"))
            f=float(input("Ingrese Precio Por Unidad:"))
            g=float(input("Ingrese Peso de Unidad:"))
            h=int(input("Ingrese cantidad de unidades"))
            objeto = Embalaje(a,b,c,d,e,f,g,h)
            self.agregar_al_final(objeto)
        else:
            print("Opcion Invalida")
    def inciso_2(self):
        if self.__tope > 1:
            lista=[]
            for servicio in self:
                lista.append(servicio)
            lista = sorted(lista)
            total_recaudado = 0
            print("Contratante\tCosto Total")
            for servicio in lista:
                print(servicio)
                total_recaudado += servicio.costo_total()
            print(f"Total Recaudado:{total_recaudado}")
            del lista
            
    def inciso_3(self):
        actual = self.__comienzo
        cant=0
        while actual:
            if isinstance(actual.objeto,Embalaje):
                if actual.objeto.peso > 50:
                    cant+=1
            actual = actual.siguiente
        print(f"La cantidad de servicios de embalaje cuyo peso por unidad supero los 50kg son {cant}")
    def inciso_4(self):
        fecha= input("Ingrese fecha:")
        actual = self.__comienzo
        cont_1=0
        cont_2=0
        while actual:
            if actual.objeto.fecha == fecha: 
                if isinstance(actual.objeto,Embalaje):
                    cont_1 +=1
                else:
                    cont_2 +=1
            actual = actual.siguiente
        if cont_1 > cont_2:
            print("El servicio Mas contratado fue el de Embalaje")
        else:
            print("El servicio mas contratado fue el de Transporfe")
    
            