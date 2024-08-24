class alquiler:
    __nom: str
    __idCancha: str
    __hora: str
    __min: str
    __duracion: int
    def __init__(self, n, i, h, m, d):
        self.__nom=n
        self.__idCancha=i
        self.__hora=h
        self.__min=m
        self.__duracion=d
    def getId(self):
        return self.__idCancha
    def getDuracion(self):
        return self.__duracion
    def getHora(self):
        return self.__hora
    def getMin(self):
        return self.__min
    def __gt__(self, otro):
        return (self.__hora+self.__min)>(otro.__hora+otro.__min)