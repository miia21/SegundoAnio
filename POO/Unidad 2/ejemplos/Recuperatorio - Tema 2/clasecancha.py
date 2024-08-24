class cancha:
    __identificador=str
    __tipopiso=str
    __importe=int

    def __init__(self,ide,tipo,imp):
        self.__identificador=ide
        self.__tipopiso=tipo
        self.__importe=imp

    def getidentificador(self):
        return self.__identificador
    def gettipopiso(self):
        return self.__tipopiso
    def getimporte(self):
        return self.__importe