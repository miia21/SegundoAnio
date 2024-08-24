class moto:
    __patente: str
    __marca: str
    __nya: str
    __kilometraje: float
    def __init__(self, p, m, n, k):
        self.__patente=p
        self.__marca=m
        self.__nya=n
        self.__kilometraje=k
    def getPatente(self):
        return self.__patente
    def getMarca(self):
        return self.__marca
    def getNya(self):
        return self.__nya
    def getKilometraje(self):
        return self.__kilometraje
    def mostrDatos(self):
        print(f"Patente: {self.__patente}\nMarca: {self.__marca}\nNombre y Apellido: {self.__nya}\nKilometraje: {self.__kilometraje}\n")
    def __it__(self, otro):
        return (self.__patente<otro.getPatente())