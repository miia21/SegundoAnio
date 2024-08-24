from claseDepartamento import departemento

class Edificio:
    #Nombre/Direccio/NombreEmpresa/CantidadPisos/CantidadDepartamento/Departamento
    __idEdificio : int
    __Nombre : str
    __Dire : str
    __nomEmp : str
    __CantPisos : int
    __CantDepar : int
    __Depa : list
    def __init__(self,id,nom,di,nomem,cP,cD):
        self.__idEdificio = id
        self.__Nombre = nom
        self.__Dire = di
        self.__nomEmp = nomem
        self.__CantPisos = cP
        self.__CantDepar = cD
        self.__Depa = []
    def setDepa (self,idDepa,nomyape,NumPiso,NumDepa,canthabita,cantbaños,superfi):
        #identificaion/NOMBRE y APELLIDO/NUMERO DE PISOS/NUMERO DE DEPARTAMENTO/CANTIDAD HABITACION/CANTIDAD BAÑOS/SUPERFICIE
        depa = departemento(idDepa,nomyape,NumPiso,NumDepa,canthabita,cantbaños,superfi)
        self.__Depa.append(depa)
    def getId (self):
        return self.__idEdificio
    def getNombre (self):
        return self.__Nombre
    def getDireccion (self):
        return self.__Dire
    def getNomEmpre (self):
        return self.__nomEmp
    def getCantiPisos (self):
        return self.__CantPisos
    def getCantDepa (self):
        return self.__CantDepar
    
    def mostrarDepartamento(self):
        #long = len(self.__Depa)
        print("----------------------------------------------------------------")
        print("ID de Edificio : ",self.getId())
        print("Nombre del Edificio es : ",self.getNombre())
        print("La direccion del Edificio es : ",self.getDireccion())
        print("Nombres de la empresa : ",self.getNomEmpre())
        print("Cantidad de pisos : ",self.getCantiPisos())
        print("Cantidad de Departamentos : ",self.getCantDepa())
        for i in range(len(self.__Depa)):
            print("Identificacion del departamento : ",self.__Depa[i].getiden())
            print("Nombre y apeliido del Propietario : ",self.__Depa[i].getnomyape())
            print("Numero de Piso : ",self.__Depa[i].getnumPiso())
            print("Numero del Departamento : ",self.__Depa[i].getnumDepa())
            print("Cantidad de Habitaciones : ",self.__Depa[i].getcantHabita())
            print("Cantidad de baños : ",self.__Depa[i].getCantBañ())
        return

    def MostrarInquilinos (self):
        for i in range(len(self.__Depa)):
            print("El nombre del Propietario es : ",self.__Depa[i].getnomyape())
        return

    def calcular (self):
        acum = 0
        for i in range(len(self.__Depa)):
            acum += self.__Depa[i].getSuper()
        return acum
    
    def SupPropi (self,nom):
        sum = 0
        for i in range(len(self.__Depa)):
            if nom == self.__Depa[i].getnomyape():
                print("El Propietario ",self.__Depa[i].getnomyape()," tiene un departamento con una superficie de ",self.__Depa[i].getSuper())
                sum += self.__Depa[i].getSuper()
        return sum
    
    def BuscraPro (self,nom):
        i=0
        ban = False
        while i < len(self.__Depa) and ban!=True:
            if nom == self.__Depa[i].getnomyape():
                ban = True
            else:
                i+=1
        return ban
    
    def MostrarPiso (self,num):
        cont = 0
        for i in range(len(self.__Depa)):
            if num == self.__Depa[i].getnumPiso():
                if self.__Depa[i].getcantHabita() > 2:
                    if self.__Depa[i].getCantBañ() > 1:
                        cont += 1
        return cont