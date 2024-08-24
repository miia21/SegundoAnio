class ViajeroFrecuente:
    def __init__(self, num_viajero=0, dni=0, nombre=0, apellido=0, millas=0):
        self.__num_viajero = num_viajero
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millas = millas
    def getNumViajero(self):
        return self.__num_viajero
    def getDNI(self):
        return self.__dni
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getMillasAcum(self):
        return self.__millas
    def setAcum(self, nuevo):
        self.__millas += nuevo
    def setAcumMenos(self, menos):
        self.__millas -= menos
    