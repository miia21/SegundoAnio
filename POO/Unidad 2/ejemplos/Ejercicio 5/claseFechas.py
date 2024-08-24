#De cada Fecha de fútbol se registran: fecha del partido, identificador de equipo local, identificador
#de equipo visitante, cantidad de goles que hizo el equipo local, cantidad de goles que hizo el equipo
#visitante.

class Fecha:
    __fecha: str
    __IdLocal: int
    __IdVisitante: int
    __GolesLocal: int
    __GolesVisitante: int
    def __init__(self, fecha=0, IdLocal = 0, IdVisitante=0, GolesLocal=0,GolesVisitante=0):
        self.__fecha = fecha
        self.__IdLocal = IdLocal
        self.__IdVisitante = IdVisitante
        self.__GolesLocal = GolesLocal
        self.__GolesVisitante = GolesVisitante
    def getFecha(self):
        return self.__fecha
    def getIdLocal(self):
        return self.__IdLocal
    def getIdVisitante(self):
        return self.__IdVisitante
    def getGolesLocal(self):
        return int(self.__GolesLocal)
    def getGolesVisitante(self):
        return int(self.__GolesVisitante)
    def mostrar(self):
        print(f"{self.__fecha} {self.__IdLocal} {self.__IdVisitante} {self.__GolesLocal} {self.__GolesVisitante}")