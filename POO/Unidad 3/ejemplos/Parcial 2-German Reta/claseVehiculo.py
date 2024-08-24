class Vehiculo:
    __marca: str
    __modelo: str
    __Fabricacion: str
    __capacidad: int
    __numero: int
    __distancia: float
    __tarifaBase: float
    def __init__(self,marca=0,modelo=0,Fabricacion=0,capacidad=0,numero=0,distancia=0,tarifaBase=0,tipoServ=0,Turno=0,tipoCarro=0):
        self.__marca = marca
        self.__modelo = modelo
        self.__Fabricacion = Fabricacion
        self.__capacidad = capacidad
        self.__numero = numero
        self.__distancia = distancia
        self.__tarifaBase = tarifaBase
    def getMarca(self):
        return self.__marca
    def getModelo(self):
        return self.__modelo
    def getFabricacion(self):
        return self.__Fabricacion
    def getCapacidad(self):
        return self.__capacidad
    def getNumero(self):
        return self.__numero
    def getDistancia(self):
        return self.__distancia
    def getTarifaBase(self):
        return float(self.__tarifaBase)