class alquiler:
    __nombre=str
    __identificador=str
    __hora=str
    __min=str
    __duracion=int

    def __init__(self,nomb,ide,hora,min,dur):
        self.__nombre=nomb
        self.__identificador=ide
        self.__hora=hora
        self.__min=min
        self.__duracion=dur

    def getnombre(self):
        return self.__nombre
    def getidentificador(self):
        return self.__identificador
    def gethora(self):
        return self.__hora
    def getmin(self):
        return self.__min
    def getduracion(self):
        return self.__duracion
    def __str__(self):
        return f"{self.__nombre, self.__identificador, self.__hora,self.__min}"
    def __gt__(self,otro):
        return (self.__hora+self.__min)>(otro.gethora()+otro.getmin())