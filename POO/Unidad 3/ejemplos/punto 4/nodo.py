class Nodo:
    __sig:object
    __datos:object
   
    def __init__(self,sig,datos):
        self.__sig=sig
        self.__datos=datos
      
    def getdatos(self):
        return self.__datos
    def getSig(self):
        return self.__sig
    def setSig(self, nodo):
        self.sig = nodo