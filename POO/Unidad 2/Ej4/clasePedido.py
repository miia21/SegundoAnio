class pedido:
    __patente: str
    __id: int
    __comida: str
    __tiempoE: int
    __tiempoR: int
    __precio: float
    def __init__(self, patente, identificador, comida, tiempoe, precio=0):
        self.__patente=patente
        self.__id=identificador
        self.__comida=comida
        self.__tiempoE=tiempoe
        self.__tiempoR=0
        self.__precio=precio
    def getPatente(self):
        return self.__patente
    def getId(self):
        return self.__id
    def getComida(self):
        return self.__comida
    def getTiempoE(self):
        return self.__tiempoE
    def getTiempoR(self):
        return self.__tiempoR
    def getPrecio(self):
        return self.__precio
    def mostrarDatos(self):
        print(f"Patente: {self.__patente}\nId: {self.__id}\nComida: {self.__comida}\nTiempo de espera estimado: {self.__tiempoE}\nTiempo de espera real: {self.__tiempoR}\nPrecio: {self.__precio}\n")
    def __it__(self, otro):
        return (self.__patente<otro.getPatente())
    