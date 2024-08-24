from claseAutobuses import Autobuses
from claseVanes import Vanes
from claseVehiculo import Vehiculo
import csv 

class gestorVehiculo:
    def __init__(self):
        self.__vehiculos = []
    def cargaVehiculo(self):
        with open('C:\\Users\\germi\\Desktop\\POO 2nd Impact\\Parcial 2-German Reta\\vehiculos.csv') as archi:
            leer = csv.reader(archi, delimiter = ';')
            next(leer)
            for vehiculo in leer:
                if vehiculo[0] == 'A':
                    autobus = Autobuses(vehiculo[1],vehiculo[2],vehiculo[3],vehiculo[4],vehiculo[5],vehiculo[6],vehiculo[7],vehiculo[8],vehiculo[9])
                    self.__vehiculos.append(autobus)
                elif vehiculo[0] == 'V':
                    van = Vanes(vehiculo[1],vehiculo[2],vehiculo[3],vehiculo[4],vehiculo[5],vehiculo[6],vehiculo[7],vehiculo[8])
                    self.__vehiculos.append(van)
    def agregarVehiculo(self):
        letra = input("Ingresar V si es una Van, A si es un autobus: ")
        try:
            letra = str(letra)
        except ValueError:
            print(f"Error, no ingresar numeros")
        else:
            if letra.lower() == 'v':
                marca = input("Ingresar la marca del vehiculo: ")
                modelo = input("Ingresar el modelo del vehiculo: ")
                fabricacion = input("Ingresar el ano de fabricacion del vehiculo: ")
                capacidad = input("Ingresar la capacidad de pasajeros del vehiculo: ")
                numero = input("Ingresar el numero de plazas del vehiculo: ")
                distancia = input("Ingresar la distancia recorrida: ")
                tarifa = input("Ingresar la tarifa base del vehiculo: ")
                tipoCarro = input("Ingresar el tipo de van que es el vehiculo, minivan o van: ")
                van = Vanes(marca,modelo,fabricacion,capacidad,numero,distancia,tarifa,tipoCarro,marca)
                self.__vehiculos.append(van)
                print("Van ingresada con exito")
            elif letra.lower() == 'a':
                marca = input("Ingresar la marca del vehiculo: ")
                modelo = input("Ingresar el modelo del vehiculo: ")
                fabricacion = input("Ingresar el ano de fabricacion del vehiculo: ")
                capacidad = input("Ingresar la capacidad de pasajeros del vehiculo: ")
                numero = input("Ingresar el numero de plazas del vehiculo: ")
                distancia = input("Ingresar la distancia recorrida: ")
                tarifa = input("Ingresar la tarifa base del vehiculo: ")
                tipoServ = input("Ingresar el tipo de servicio del autobus, interurbano, turismo , etc: ")
                Turno = input("Ingresar el turno, manana, tarde o noche: ")
                autobus = Autobuses(marca,modelo,fabricacion,capacidad,numero,distancia,tarifa,tipoServ,Turno)
                self.__vehiculos.append(autobus)
                print("Autobus ingresado con exito")
            else:
                print(f"ERROR. Ingresar un caracter valido...\n")
    def mostrarTipo(self):
        i = input("Ingresar el numero del vehiculo que desea saber su tipo: ")
        try:
            i = int(i)
        except ValueError:
            print("Error, solo puede ingresar numeros...")
        else:
            if isinstance(self.__vehiculos[i],Vanes):
                return print(f"El vehiculo es una Van {self.__vehiculos[i].getModelo()}")
            elif isinstance(self.__vehiculos[i],Autobuses):
                return print(f"El vehiculo es un Autobus {self.__vehiculos[i].getModelo()}")
    def contarCant(self):
        contVan = 0
        contBus = 0
        for vehiculo in self.__vehiculos:
            if isinstance(vehiculo,Vanes):
                contVan += 1
            elif isinstance(vehiculo,Autobuses):
                contBus += 1
        print(f"Hay {contVan} Vanes en la lista y {contBus} Autobuses")
    def mostrar(self):
        for vehiculo in self.__vehiculos:
            if isinstance(vehiculo, Autobuses):
                print(f"{vehiculo.getModelo()}   {vehiculo.getFabricacion()}    {vehiculo.getCapacidad()}   {vehiculo.getTarifa()} ")   
            elif isinstance(vehiculo, Vanes):
                print(f"{vehiculo.getModelo()}   {vehiculo.getFabricacion()}    {vehiculo.getCapacidad()}   {vehiculo.getTarifa()} ")   
