from claseCliente import cliente
import csv

class gestorCliente:
    __clientes: list
    def __init__(self):
        self.__clientes=[]
    #C:\\Users\\admin\\Desktop\\facuu\\2do año\\codigos\\practica
    def cargar(self):
        with open('G:\\Otros ordenadores\\Escritorio\\facuu\\2do año\\codigos\\practica mal\\ClientesFarmaCiudad.csv') as archivo:
            leer=csv.reader(archivo, delimiter=';')
            next(leer)
            for fila in leer:
                c=cliente(fila[0], fila[1], fila[2], fila[3], fila[4])
                self.__clientes.append(c)
    def mostrar(self, xi):
        print(f"Cliente: {self.__clientes[xi].getAp()}, {self.__clientes[xi].getNom()}      Numero de Cuenta: {self.__clientes[xi].getNum()}\nSaldo anterior: {self.__clientes[xi].getSal()}")
    def buscarCuenta(self, xdni):
        x=False
        i=0
        while x==False and i<len(self.__clientes):
            if xdni==self.__clientes[i].getDni():
                x=True
                return i
            else:
                i=i+1
        i=-1
        return i
    def actualizar(self, a):
        dni=input("Ingrese un dni\n")
        i=self.buscarCuenta(dni)
        if i!=-1:
            num=self.__clientes[i].getNum()
            self.mostrar(i)
            acum=a.buscarMov(num)
            self.__clientes[i].setSal(self.__clientes[i].getSal()+acum)
            print(f"Saldo actualizado: {self.__clientes[i].getSal()}")
        else:
            print("No se encontro el cliente")
    def movimientos(self, a):
        dni=input("Ingrese un dni\n")
        i=self.buscarCuenta(dni)
        if i!=-1:
            num=self.__clientes[i].getNum()
            x=a.buscarNum(num)
            if x==0:
                print(f"El cliente {self.__clientes[i].getAp()}, {self.__clientes[i].getNom()} no realizo movimientos en el mes de abril")
            else:
                print("EL cliente si realizo movimientos en el mes de abril")
        else:
            print("No se encontro el cliente")