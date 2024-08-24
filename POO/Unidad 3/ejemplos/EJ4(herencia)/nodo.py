class nodo:
    __publicacion: object
    __sig: object
    def __init__(self,publicacion):
        self.__publicacion=publicacion
        self.__sig=None
    def setSiguiente(self,siguiente):
        self.__sig=siguiente
    def getSiguiente(self):
        return self.__sig
    def getpublicacion(self):
        return self.__publicacion