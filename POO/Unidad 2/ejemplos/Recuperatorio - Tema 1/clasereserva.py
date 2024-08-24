class reserva:
    __nroreserva=int
    __nombre=str
    __nrocabaña=int
    __fechainicio=str
    __canthuespedes=int
    __cantdias=int
    __importeseña=float

    def __init__(self,nrores,nomb,nrocab,fecha,canthues,dias,impse):
        self.__nroreserva=nrores
        self.__nombre=nomb
        self.__nrocabaña=nrocab
        self.__fechainicio=fecha
        self.__canthuespedes=canthues
        self.__cantdias=dias
        self.__importeseña=impse

    def getnroreserva(self):
        return self.__nroreserva
    def getnombre(self):
        return self.__nombre
    def getnrocabaña(self):
        return self.__nrocabaña
    def getfechainicio(self):
        return self.__fechainicio
    def getcanthuespedes(self):
        return self.__canthuespedes
    def getcantidaddias(self):
        return self.__cantdias
    def getimporteseña(self):
        return self.__importeseña
