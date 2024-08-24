from clase_servicio import Servicio

class Nodo:
    __objeto : Servicio
    __siguiente : object
    
    def __init__(self,objeto):
        self.__objeto = objeto
        self.__siguiente = None
    @property
    def objeto(self):
        return self.__objeto
    @objeto.setter
    def objeto(self,new):
        self.__objeto = new
    @property
    def siguiente(self):
        return self.__siguiente
    @siguiente.setter
    def siguiente(self,new):
        self.__siguiente = new