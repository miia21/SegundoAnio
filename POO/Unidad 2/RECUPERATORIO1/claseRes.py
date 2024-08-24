class reserva:
    __num: int
    __nom: str
    __numcab: int
    __fecha: str
    __canthues: int
    __cantdias: int
    __sena: float
    def __init__(self, nu, no, num, fe, ch, cd, s):
        self.__num=nu
        self.__nom=no
        self.__numcab=num
        self.__fecha=fe
        self.__canthues=ch
        self.__cantdias=cd
        self.__sena=s
    def getNumcab(self):
        return self.__numcab
    def getFecha(self):
        return self.__fecha
    def getCantd(self):
        return self.__cantdias
    def getSena(self):
        return self.__sena
