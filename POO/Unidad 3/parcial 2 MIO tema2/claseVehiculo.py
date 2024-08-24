class vehiculo:
    __marca: str
    __modelo: str
    __anio: str
    __capacidad: int
    __numPlaza: int
    __distancia: float
    __tarifa: float
    def __init__(self, marca, modelo, anio, capacidad, num, dis, tari):
        self.__marca=marca
        self.__modelo=modelo
        self.__anio=anio
        self.__capacidad=capacidad
        self.__numPlaza=num
        self.__distancia=dis
        self.__tarifa=tari
    def getTarifa(self):
        return self.__tarifa
    def tarifa(self):
        pass
    def mostrar(self):
        print(f"---------\nModelo: {self.__modelo}\nAño de fabricacion: {self.__anio}\nCapacidad: {self.__capacidad}\nTarifa: {self.tarifa()}")