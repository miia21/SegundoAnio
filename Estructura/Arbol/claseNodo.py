class nodo:
    __objeto: object
    __cant: int
    __der: object
    __izq: object

    def __init__(self, objeto):
        self.__objeto=objeto
        self.__cant=1
        self.__der=None
        self.__izq=None

    def getObjeto(self):
        return self.__objeto
    
    def setObjeto(self, objeto):
        self.__objeto=objeto

    def getCant(self):      
        return self.__cant
    
    def setCant(self, cant):
        self.__cant=cant

    def setDerecha(self,der):
        self.__der=der

    def getDerecha(self):
        return self.__der
    
    def setIzquierda(self,izq):
        self.__izq=izq

    def getIzquierda(self):
        return self.__izq
    
