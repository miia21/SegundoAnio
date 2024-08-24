import csv
from claseNodo import nodo
from claseServicioEmbalaje import servicioEmbalaje
from claseServicioTransporte import servicioTransporte

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
            dato = self.__actual.getServicio()
            self.__actual = self.__actual.getSiguiente()
            return dato
    def agregarFinal(self,objeto):
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
    def carga(self):
        archivo=open("C:\\Users\\admin\\Desktop\\facuu\\2do año\\codigos\\Unidad 3\\PARCIAL MIO\\transporte.csv")
        leer=csv.reader(archivo,delimiter=';')
        next(leer)
        for fila in leer:
            servi=servicioTransporte(fila[0], fila[1], fila[2], fila[3], float(fila[4]), precio=float(fila[5]), peso=float(fila[6]), cantidad=int(fila[7]), direccion=fila[8])
            self.agregarFinal(servi)
        archivo.close()
        archivo2=open("C:\\Users\\admin\\Desktop\\facuu\\2do año\\codigos\\Unidad 3\\PARCIAL MIO\\embalaje.csv")
        leer=csv.reader(archivo2,delimiter=';')
        next(leer)
        for fila in leer:
            servi2=servicioEmbalaje(fila[0], fila[1], fila[2], fila[3], float(fila[4]), precio=float(fila[5]), peso=float(fila[6]), cantidad=int(fila[7]))
            self.agregarFinal(servi2)
        archivo2.close()
    def agregar(self):
        print("1- Agregar transporte\n2- Agregar embalaje\n3- Salir\n")
        o=int(input("Ingrese una opcion\n"))
        while(o!=3):
            if (o==1):
                nom1=input("ingresar el nombre de la empresa: \n")
                nom2=input("ingresar el nombre del contratista: \n")
                dir=input("ingresar la direccion: \n")
                fecha=input("ingresar la fecha: \n")
                com=float(input("ingresar la comision: \n"))
                pre=float(input("ingresar precio por hora: \n"))
                pes=float(input("ingresar peso: \n"))
                dire=input("ingresar direccion de destino: \n")
                untrans=servicioTransporte(nom1,nom2,dir,fecha,com, precio=pre, peso=pes, direccion=dire)
                self.agregarFinal(untrans)
            elif (o==2):
                nom1=input("ingresar el nombre de la empresa: \n")
                nom2=input("ingresar el nombre del contratante: \n")
                dir=input("ingresar la direccion: \n")
                fecha=input("ingresar la fecha: \n")
                com=float(input("ingresar la comision: \n"))
                pre=float(input("ingresar precio por hora: \n"))
                pes=float(input("ingresar peso: \n"))
                cant=int(input("ingresar cantidad: \n"))
                unemba=servicioEmbalaje(nom1,nom2,dir,fecha,com, precio=pre, peso=pes, cantidad=cant)
                self.agregarFinal(unemba)
            else:
                print("opcion incorrecta\n")
            print("1- Agregar transporte\n2- Agregar embalaje\n3- Salir\n")
            o=int(input("Ingrese una opcion\n"))
    def ordenar(self):
        if self.__comienzo is None or self.__comienzo.getSiguiente() is None:
            return
        actual = self.__comienzo
        while actual.getSiguiente() is not None:
            siguiente = actual.getSiguiente()
            while siguiente is not None:
                if isinstance(actual.getServicio(), servicioTransporte) and isinstance(siguiente.getServicio(), servicioTransporte):
                    if actual.getServicio() > siguiente.getServicio():
                        aux = actual.getServicio()
                        actual.setServicio(siguiente.getServicio())
                        siguiente.setServicio(aux)
                siguiente = siguiente.getSiguiente()
            actual = actual.getSiguiente()
    def mostrar(self):
        self.ordenar()
        x=0
        aux=self.__comienzo
        print("Contratante          Costo total\n")
        while aux is not None:
            if isinstance(aux.getServicio(),servicioTransporte):
                print(f"{aux.getServicio().getNomCont()}             {aux.getServicio().costoTotal()}\n")
                x+=aux.getServicio().costoTotal()
            aux=aux.getSiguiente()
        print(f"Total: {x}")
    def cantidad(self):
        cont=0
        aux=self.__comienzo
        while (aux!= None):
            P=aux.getServicio()
            if isinstance(P,servicioEmbalaje) and P.getPeso()>50:
                cont+=1
            aux=aux.getSiguiente()
        print(f"La cantidad de servicios de embalaje que superan los 50kg son: {cont}\n")
    def fecha(self):
        xfecha=input("Ingrese una fecha\n")
        aux=self.__comienzo
        cont1=0
        cont2=0
        while aux!=None:
            if aux.getServicio().getFecha() == xfecha: 
                if isinstance(aux.getServicio(), servicioTransporte):
                    cont1 +=1
                else:
                    cont2 +=1
            aux = aux.getSiguiente()
        if cont1 > cont2:
            print("El servicio Mas contratado fue el de Transporte")
        else:
            print("El servicio mas contratado fue el de Embalaje")
