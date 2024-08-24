from claseCuentas import cuentas
import numpy as np
import csv
from GestorTransacciones import controlaT
class GestorC:
    __cuentas: np.ndarray

    def __init__(self,incremento=1,dimension=1,cantidad=1):

        self.__cuentas= np.array([],dtype=cuentas)
    def test(self):
        archivo=open('G:\\Otros ordenadores\\Mi portátil\\POO\\U2\\EJ6\\cuentasBilletera.csv')
        leer=csv.reader(archivo,delimiter=';')
        next(leer)
        for fila in leer:
            apellido=fila[0]
            nombre=fila[1]
            dni=fila[2]
            telefono=int(fila[3])
            saldo=float(fila[4])
            cvu=int(fila[5])
            unacuenta=cuentas(apellido,nombre,dni,telefono,saldo,cvu)
            self.__cuentas=np.append(self.__cuentas,unacuenta)
        archivo.close()

    def mostrardat(self):
        dni=input("ingresar DNI del cliente: ")
        i=0
        t=controlaT()
        k=len(self.__cuentas)
        while ((i<k) and (dni!=self.__cuentas[i].getdni())):
            i+=1
        
        if(i<k):
            cvu=self.__cuentas[i].getcvu()
            saldo=self.__cuentas[i].getsaldo()
            nuevosaldo = t.modisaldo(cvu) + saldo
            self.__cuentas[i].modifsaldo(nuevosaldo)
            print(f"Apellido: {self.__cuentas[i].getapellido()}\nNombre: {self.__cuentas[i].getnombre()}\nCVU: {self.__cuentas[i].getcvu()}\nsaldo: {self.__cuentas[i].getsaldo()}")
        else:
            print("no se encontro la cuenta")
    def modifA(self):
        porcentaje=float(input("ingresar nuevo porcentaje anual: "))
        porcentaje=porcentaje/365
        i=0
        cuentas.porcentajeA=porcentaje
    def guardarcuentas(self):
        archivo=open("cuentasActualizadas.csv","w", newline="")
        writer=csv.writer(archivo,delimiter=";")
        writer.writerow(["Apellido","Nombre","dni","telefono","saldo","cvu",])
        for i in range (len(self.__cuentas)):
            ap=self.__cuentas[i].getapellido()
            nomb=self.__cuentas[i].getnombre()
            dni=self.__cuentas[i].getdni()
            tel=str(self.__cuentas[i].gettelefono())
            saldo=str(self.__cuentas[i].getsaldo())
            cvu=str(self.__cuentas[i].getcvu())
            array=[ap,nomb,dni,tel,saldo,cvu]
            writer.writerow(array)
        archivo.close()
        