class movimiento:
    __nroCuenta: int
    __fecha: str
    __descripcion: str
    __tipoMov: str
    __importe: float
    def __init__(self, num, fecha, des, tipo, imp):
        self.__nroCuenta=num
        self.__fecha=fecha
        self.__descripcion=des
        self.__tipoMov=tipo
        self.__importe=imp
    def getNum(self):
        return self.__nroCuenta
    def getFecha(self):
        return self.__fecha
    def getDes(self):
        return self.__descripcion
    def getTipo(self):
        return self.__tipoMov
    def getImp(self):
        return self.__importe
    def __lt__(self,otro):
        return self.__nroCuenta < otro.getNum()
    def mostrar(self):
        print(f"Numero Cuenta: {self.__nroCuenta}\nFecha: {self.__fecha}\nDescripcion: {self.__descripcion}\nTipo de Movimiento: {self.__tipoMov}\nImporte: {self.__importe}")