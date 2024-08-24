class nodo:
    __objeto: object
    __sig: object

    def __init__(self, objeto):
        self.__objeto=objeto
        self.__sig=None

    def setSiguiente(self,siguiente):
        self.__sig=siguiente

    def getSiguiente(self):
        return self.__sig
    
    def getObjeto(self):
        return self.__objeto
    
    def setObjeto(self, objeto):
        self.__objeto=objeto