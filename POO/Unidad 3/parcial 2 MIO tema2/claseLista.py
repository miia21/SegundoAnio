from claseAuto import autobus
from claseVan import van
from claseVehiculo import vehiculo
import csv

class lista:
    __lista: list
    def __init__(self):
        self.__lista= []
    def carga(self):
        with open('C:\\Users\\admin\\Desktop\\facuu\\2do año\\codigos\\Unidad 3\\parcial 2 MIO tema2\\vehiculos.csv') as archivo:
            leer=csv.reader(archivo, delimiter=';')
            next(leer)
            for fila in leer:
                if fila[0]=='A':
                    a=autobus(fila[1], fila[2], fila[3], int(fila[4]), int(fila[5]), float(fila[6]), float(fila[7]), tipo=fila[8], turno=fila[9])
                    self.__lista.append(a)
                else:
                    v=van(fila[1], fila[2], fila[3], int(fila[4]), int(fila[5]), float(fila[6]), float(fila[7]), tipo=fila[8])
                    self.__lista.append(v)
    def agregar(self):
        print("1- Agregar autobus\n2- Agregar van\n3- Salir\n")
        o=int(input("Ingrese una opcion\n"))
        while(o!=3):
            if (o==1):
                mar=input("ingresar la marca: \n")
                mod=input("ingresar el modelo: \n")
                anio=input("ingresar el año de fabricacion: \n")
                cap=input("ingresar la capacidad: \n")
                num=float(input("ingresar el numero de plazas: \n"))
                dis=float(input("ingresar la distancia recorrida: \n"))
                tari=float(input("ingresar la tarifa base: \n"))
                tip=input("ingresar el tipo de servicio: \n")
                tur=input("ingresar el turno de servicio: \n")
                a=autobus(mar,mod,anio,cap,num, dis, tari, tipo=tip, turno=tur)
                self.__lista.append(a)
            elif (o==2):
                mar=input("ingresar la marca: \n")
                mod=input("ingresar el modelo: \n")
                anio=input("ingresar el año de fabricacion: \n")
                cap=input("ingresar la capacidad: \n")
                num=float(input("ingresar el numero de plazas: \n"))
                dis=float(input("ingresar la distancia recorrida: \n"))
                tari=float(input("ingresar la tarifa base: \n"))
                tip=input("ingresar el tipo de servicio: \n")
                v=van(mar,mod,anio,cap,num, dis, tari, tipo=tip)
                self.__lista.append(v)
            else:
                print("opcion incorrecta\n")
            print("1- Agregar autobus\n2- Agregar van\n3- Salir\n")
            o=int(input("Ingrese una opcion\n"))
    def cantPos(self):
        print(f"La lista tiene {len(self.__lista)} elementos\n")
        try:
            i=int(input("Ingrese una posicion\n"))
        except i>len(self.__lista):
            print("numero fuera de rango\n")
        if isinstance(self.__lista[i], autobus):
            print("Es un autobus\n")
        else:
            print("Es un autobus\n")
    def cantidad(self):
        cont1=0
        cont2=0
        for vehiculo in self.__lista:
            if isinstance(vehiculo,autobus):
                cont1+=1
            else:
                cont2+=1
        print(f"La cantidad de autobuses es: {cont1}\nLa cantidad de vanes es: {cont2}")
    def mostrar(self):
        for vehiculo in self.__lista:
            vehiculo.mostrar()