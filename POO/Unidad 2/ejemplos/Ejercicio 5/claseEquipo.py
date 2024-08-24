class Equipo:
    __identificador: int
    __nombre: str
    __favor: int
    __contra: int
    __diferencia: int
    __puntos: int
    def __init__(self, identificador=0, nombre=0, favor=0, contra=0,diferencia=0,puntos=0):
        self.__identificador = identificador
        self.__nombre = nombre
        self.__favor = int(favor)
        self.__contra = int(contra)
        self.__diferencia = int(diferencia)
        self.__puntos = int(puntos)
    def getIdentificador(self):
        return self.__identificador
    def getNombre(self):
        return self.__nombre
    def getFavor(self):
        return self.__favor
    def getContra(self):
        return self.__contra
    def getDiferencia(self):
        return self.__diferencia
    def getPuntos(self):
        return self.__puntos
    def setFavor(self,xfavor):
        self.__favor += int(xfavor)
    def setContra(self,xcontra):
        self.__contra += int(xcontra)
    def setDiferencia(self, xdiferencia):
        self.__diferencia += int(xdiferencia)
    def setPuntos(self,xpuntos):
        self.__puntos += int(xpuntos)
    def __gt__(self, other):
        if self.__puntos != other.__puntos:
            return self.__puntos > other.__puntos
        elif self.__diferencia != other.__diferencia:
            return self.__diferencia > other.__diferencia
        else:
            return self.__favor > other.__favor
    def mostrar(self):
        return print(f"Identificador:  {self.__identificador} \nNombre:{self.__nombre} \nGoles a favor: {self.__favor} \nGoles en Contra: {self.__contra} \nDiferencia de goles: {self.__diferencia} \nPuntos: {self.__puntos}\n\n")