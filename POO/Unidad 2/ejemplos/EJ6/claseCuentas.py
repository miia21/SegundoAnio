class cuentas:
    __apellido= str
    __nombre=str
    __dni=str
    __telefono=int
    __saldo=float
    __cvu=int
    porcentajeA = 0.18
    def __init__(self ,apellido=0,nombre=0,dni=0,tel=0,saldo=0,cvu=0):
        self.__apellido= apellido
        self.__nombre= nombre
        self.__dni= dni
        self.__telefono= tel
        self.__saldo= saldo
        self.__cvu= cvu
    def getapellido(self):
        return self.__apellido
    def getnombre(self):
        return self.__nombre
    def getdni(self):
        return self.__dni
    def gettelefono(self):
        return self.__telefono
    def getsaldo(self):
        return self.__saldo
    def getcvu(self):
        return self.__cvu
    def modifsaldo(self,nuevo):
        self.__saldo=nuevo
    @classmethod
    def getporcentajeA(cls):
        return cls.porcentajeA
    @classmethod
    def modificaPorcentaje(cls,A):
        cls.porcentajeA=A
