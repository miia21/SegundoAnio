class nodo:
    __planes: object
    __sig: object
    def __init__(self, planes):
        self.__planes=planes
        self.__sig=None
    def setSiguiente(self,siguiente):
        self.__sig=siguiente
    def getSiguiente(self):
        return self.__sig
    def getPlanes(self):
        return self.__planes
    def setPlanes(self, planes):
        self.__planes=planes