class cabaña:
    __numero=int
    __canthabitaciones=int
    __cantcamasgrandes=int
    __cantcamaschicas=int
    __importe=float

    def __init__(self,num,canthab,cantcg,cantcc,imp):
        self.__numero=num
        self.__canthabitaciones=canthab
        self.__cantcamasgrandes=cantcg
        self.__cantcamaschicas=cantcc
        self.__importe=imp

    def getnumero(self):
        return self.__numero
    def getcanthab(self):
        return self.__canthabitaciones
    def getcantcamg(self):
        return self.__cantcamasgrandes
    def getcantcamc(self):
        return self.__cantcamaschicas
    def getimporte(self):
        return self.__importe
    def __ge__(self,otro):
        return self.__numero >= otro.getnumero()