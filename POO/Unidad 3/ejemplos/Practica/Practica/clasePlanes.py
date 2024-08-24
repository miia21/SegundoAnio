import abc
from abc import ABC

class Planes(ABC):
    __nombComp: str
    __duracion: str
    __cobertura: str
    __precioBase: float
    def __init__(self,nombComp=0,duracion=0,cobertura=0,precioBase=0,tipoLlamada=0,cantMinutos=0,nacionales=0,internacionales=0):
        self.__nombComp = nombComp
        self.__duracion = duracion
        self.__cobertura = cobertura
        self.__precioBase = precioBase
    def getNomb(self):
        return self.__nombComp
    def getDuracion(self):
        return self.__duracion
    def getCobertura(self):
        return self.__cobertura.lower()
    def getPrecioBase(self):
        return float(self.__precioBase)
    @abc.abstractmethod
    def precio():
        pass
    
    def mostrar(self):
        print(f"Nombre de la compañia:{self.getNomb()}\nDuracion:{self.getDuracion()}\nCobertura:{self.getCobertura()}\nImporte Final:{self.precio()}\n")