import datetime

class jugador:
    __nombre: str
    __puntaje: int
    __fecha: datetime

    def __init__(self, nombre, puntaje, fecha):
        self.__nombre=nombre
        self.__puntaje=puntaje
        self.__fecha=fecha

    def getNombre(self):
        return self.__nombre
    
    def getPuntaje(self):
        return self.__puntaje
    
    def getFecha(self):
        return self.__fecha
    
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                nombre=self.__nombre,
                puntaje=self.__puntaje,
                fecha=self.__fecha,
                )
            )
        return d
    
    def __gt__(self, otro):
        return self.__puntaje>otro.__puntaje