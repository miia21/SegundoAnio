from claseObjeto import objeto          #Importar objetos
import csv

class gestorObjeto:
    __objetos: list
    def __init__(self):
        self.__objetos=[]
    def cargar(self):       #Carga con archivo csv
        with open('G:\\Otros ordenadores\\Escritorio\\facuu\\2do año\\codigos\\practica mal\\ClientesFarmaCiudad.csv') as archivo:
            leer=csv.reader(archivo, delimiter=';')
            next(leer)
            for fila in leer:
                o=objeto(fila[0], fila[1], fila[2], fila[3], fila[4])
                self.__objetos.append(c)
    def mostrar(self, xi):      #Mostrar elementos de la lista
        print(f"Cliente: {self.__objetos[xi].getAp()}, {self.__objetos[xi].getNom()}      Numero de Cuenta: {self.__objetos[xi].getNum()}\nSaldo anterior: {self.__objetos[xi].getSal()}")
    def buscarCuenta(self, xdni):       #Buscar elemento por atributo
        x=False
        i=0
        while x==False and i<len(self.__objetos):
            if xdni==self.__objetos[i].getDni():
                x=True
                return i
            else:
                i=i+1
        i=-1
        return i
