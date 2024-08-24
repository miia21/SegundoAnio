class cliente:
    __nombre: str
    __apellido: str
    __dni: int
    __nroCuenta: int
    __saldoAnt: float
    def __init__(self, nom, ap, dni, num, sal):
        self.__nombre=nom
        self.__apellido=ap
        self.__dni=dni
        self.__nroCuenta=num
        self.__saldoAnt=sal
    def getNom(self):
        return self.__nombre
    def getAp(self):
        return self.__apellido
    def getDni(self):
        return self.__dni
    def getNum(self):
        return self.__nroCuenta
    def getSal(self):
        return float(self.__saldoAnt)
    def setSal(self, sal):
        self.__saldoAnt=sal
    def mostrar(self):
        print(f"Nombre: {self.__nombre}\nApellido: {self.__apellido}\nDni: {self.__dni}\nNumero de Cuenta: {self.__nroCuenta}\nSaldo: {self.__saldoAnt}")