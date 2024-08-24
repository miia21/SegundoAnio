from abc import ABC, abstractmethod
class Servicio(ABC):
    __nombre:str
    __contratante:str
    __direccion:str
    __fecha:str
    __comision:str
    def __init__(self,nombre,contratante,direccion,fecha,comision):
        self.__nombre=nombre
        self.__contratante=contratante
        self.__direccion=direccion
        self.__fecha=fecha
        self.__comision=comision
    @property
    def nombre(self):
        return self.__nombre
    @property
    def contratante(self):
        return self.__contratante
    @property
    def direccion(self):
        return self.__direccion
    @property
    def fecha(self):
        return self.__fecha
    @property
    def comision(self):
        return self.__comision