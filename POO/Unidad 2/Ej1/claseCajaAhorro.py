class cajaAhorro:
    __nroCuenta:int
    __cuil:str
    __apellido:str
    __nombre:str
    __saldo:float
    def __init__(self, nroCuenta, cuil, apellido, nombre, saldo):
        self.__nroCuenta=nroCuenta
        self.__cuil=cuil
        self.__apellido=apellido
        self.__nombre=nombre
        self.__saldo=saldo
    def setSaldo(self, saldo):
        self.__saldo=saldo
    def mostrarDatos(self):
        print(f"Número de cuenta:{self.__nroCuenta}")
        print(f"Cuil:{self.__cuil}")
        print(f"Apellido:{self.__apellido}")
        print(f"Nombre:{self.__nombre}")
        print(f"Saldo:{self.__saldo}")
    def extraer(self, imp):
        if imp<=self.__saldo:
            self.setSaldo(self.__saldo-imp)
            print(f"El saldo restante es: {self.__saldo}")
        else:
            print(f"No se puede realizar la extraccion")
    def depositar(self, imp):
        if imp>0:
            self.setSaldo(self.__saldo+imp)
            print(f"El saldo total es: {self.__saldo}")
        else:
            print(f"No se puede depositar un importe negativo")
    def validarCuil(self):
        if len(self.__cuil) != 13 or self.__cuil[2] != "-" or self.__cuil[11] != "-":
            return False
        cuil_sin_guion = self.__cuil.replace("-", "")
        base = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
        aux = 0
        for i in range(10):
            aux += int(cuil_sin_guion[i]) * base[i]
        aux = 11 - (aux - (int(aux / 11) * 11))
        if aux == 11:
            aux = 0
        if aux == 10:
            aux = 9
        return aux == int(cuil_sin_guion[10])
    