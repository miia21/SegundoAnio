class clasePuntaje:
    __dni:int
    __estilo:str
    __puntaje1:float
    __puntaje2:float
    __puntaje3:float

    def __init__(self,dni,estilo,p1,p2,p3):
        self.__dni=dni
        self.__estilo=estilo
        self.__puntaje1=p1
        self.__puntaje2=p2
        self.__puntaje3=p3
    
    def __str__(self):
        return f"DNI:{self.__dni}\nEstilo:{self.__estilo}\nPuntaje 1:{self.__puntaje1}\nPuntaje 2:{self.__puntaje2}\nPuntaje 3:{self.__puntaje3}\n"
    
    def getEstilo(self):
        return self.__estilo
    
    def getDNI(self):
        return self.__dni