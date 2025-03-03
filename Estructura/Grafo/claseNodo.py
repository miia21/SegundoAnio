class nodo:
    __destino: object
    __peso: int
    __sig: object

    def __init__(self, destino, peso):
        self.__destino=destino
        self.__peso=peso
        self.__sig=None

    def setSiguiente(self,siguiente):
        self.__sig=siguiente

    def getSiguiente(self):
        return self.__sig
    
    def getDestino(self):
        return self.__destino
    
    def setDestino(self, destino):
        self.__destino=destino

    def getPeso(self):
        return self.__peso
    
    def setPeso(self, peso):
        self.__peso=peso