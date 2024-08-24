
class departemento:
    #identificaion/NOMBRE y APELLIDO/NUMERO DE PISOS/NUMERO DE DEPARTAMENTO/CANTIDAD HABITACION/CANTIDAD BAÑOS/SUPERFICIE
    __idDepa : int
    __nomyape : str
    __NumPiso : int
    __NumDepa : int
    __canthabita : int
    __cantbaños: int
    __superfi : float
    def __init__(self,id,na,nuP,numD,cH,cB,sup):
        self.__idDepa = id
        self.___nomyape = na
        self.__NumPiso = nuP
        self.__NumDepa = numD
        self.__canthabita = cH
        self.__cantbaños = cB
        self.__superfi = sup
    def getiden (self):
        return self.__idDepa
    def getnomyape (self):
        return self.___nomyape
    def getnumPiso (self):
        return self.__NumPiso
    def getnumDepa (self):
        return self.__NumDepa
    def getcantHabita (self):
        return self.__canthabita
    def getCantBañ (self):
        return self.__cantbaños
    def getSuper (self):
        return self.__superfi
