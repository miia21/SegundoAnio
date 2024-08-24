class transaccion:
    __cvu=int
    __nro=int
    __importe=float
    __tipo=str
    def __init__(self,cvu,num,importe,tipo):
        self.__cvu=cvu
        self.__nro=num
        self.__importe=importe
        self.__tipo=tipo
    def getcvu(self):
        return self.__cvu
    def getnro(self):
        return self.__nro
    def getimporte(self):
        return self.__importe
    def gettipo(self):
        return self.__tipo