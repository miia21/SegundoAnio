class nodoCursor:
    __objeto: object
    __sig: int

    def __init__(self, objeto, siguiente=None):
        self.__objeto=objeto
        self.__sig=siguiente

    def setSiguiente(self,siguiente):
        self.__sig=siguiente

    def getSiguiente(self):
        return self.__sig
    
    def getObjeto(self):
        return self.__objeto
    
    def setObjeto(self, objeto):
        self.__objeto=objeto