class nodo:
    __servicio: object
    __sig: object
    def __init__(self, servicio):
        self.__servicio=servicio
        self.__sig=None
    def setSiguiente(self,siguiente):
        self.__sig=siguiente
    def getSiguiente(self):
        return self.__sig
    def getServicio(self):
        return self.__servicio
    def setServicio(self, servicio):
        self.__servicio=servicio
        