from claseViajeroFrecuente import ViajeroFrecuente
import csv

class lista:
    def __init__ (self):
        self.__lista=[]
    def cargaLista (self):
        with open ('C:\\Users\\germi\\Desktop\\POO\\Unidad 2\\Ejercicio 2\\Viajeros.csv') as archivo:
            leer = csv.reader (archivo)
            for raw in leer:
                viajero = ViajeroFrecuente (int(raw[0]), raw[1], raw[2], raw[3], float(raw[4]))
                self.__lista.append(viajero)
    def mostraViajeros(self):
        for i in range(len(self.__lista)):
            mos = self.__lista[i]
            print(f"El numero del viajero numero: {i} es: {mos.getNumViajero()}")
            print(f"El DNI del viajero numero: {i} es: {mos.getDNI()}")
            print(f"El Nombre del viajero numero: {i} es: {mos.getNombre()}")
            print(f"El Apellido del viajero numero: {i} es: {mos.getApellido()}")
            print(f"La cantidad de millas acumuladas del viajero numero: {i} es: {mos.getMillasAcum()}")
    def buscarViajero(self):
        numb = int(input('Ingresar numero de viajero: '))
        i=0
        a=-1
        e=False
        while i < len(self.__lista) and not e:
            if self.__lista[i].getNumViajero() == numb:
                e = True
                a=i
            else:
                i += 1
        if e == True:
            return a
        else:
            print(f"ERROR")
    def cantidadTotaldeMillas(self,a):
         print(f"La cantidad de millas acumuladas del viajero numero: {a} es: {self.__lista[a].getMillasAcum()}")
    def acumularMillas (self,a):
        m = float(input('Ingresar la cantidad nueva de millas recoridas:'))
        self.__lista[a].setAcum(m)
        print(f"La nueva cantidad de millas acumuladas es de: {self.__lista[a].getMillasAcum()}")
    def canejarMillas (self,a):
        canje = float(input('Ingresar la cantidad de millas a canejar:'))
        if canje <= self.__lista[a].getMillasAcum():
            self.__lista[a].setAcumMenos(canje)
            print(f"El nuevo valor despues del canje es de: {self.__lista[a].getMillasAcum()}")
        else:
            print(f"ERROR DE OPERACION")