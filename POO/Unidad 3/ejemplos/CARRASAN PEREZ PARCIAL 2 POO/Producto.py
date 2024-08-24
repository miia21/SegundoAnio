import abc
from abc import ABC

class Producto(ABC):
    __nombre: str
    __fechaEnvasado: str
    __fechaVencimiento: str
    __tempMantenimiento: str
    __pais: str
    __noLote: int
    __costoBase: float

    def __init__(self, nombre: str, fechaE: str, fechaV: str, tempMant: str, pais: str, lote: str, costoB: float):
        self.__nombre = nombre
        self.__fechaEnvasado = fechaE
        self.__fechaVencimiento = fechaV
        self.__tempMantenimiento = tempMant
        self.__pais = pais
        self.__noLote = lote
        self.__costoBase = costoB

    def getNombre(self):
        return self.__nombre
    
    def getFechaE(self):
        return self.__fechaEnvasado
    
    def getFechaV(self):
        return self.__fechaVencimiento
    
    def getTempMant(self):
        return self.__tempMantenimiento
    
    def getPais(self):
        return self.__pais
    
    def getNoLote(self):
        return self.__noLote
    
    def getCostoBase(self):
        return self.__costoBase
    
    @abc.abstractmethod
    def getImporteVenta(self):
        pass

    @abc.abstractmethod
    def __str__(self):
        pass
