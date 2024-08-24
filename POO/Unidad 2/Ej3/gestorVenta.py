import numpy as np

class gestor:
    __arreglo: np.ndarray
    def __init__(self):
        self.__arreglo= np.zeros([5,7],dtype=float)
    def cargaDatos(self):
        dia=input("Ingrese el dia de la semana\n")
        if dia=="lunes":
            xdia=0
        elif dia=="martes":
            xdia=1
        elif dia=="miercoles":
            xdia=2
        elif dia=="jueves":
            xdia=3
        elif dia=="viernes":
            xdia=4
        elif dia=="sabado":
            xdia=5
        elif dia=="domingo":
            xdia=6
        suc=int(input("Ingrese la sucursal\n"))
        imp=float(input("Ingrese el importe de la venta\n"))
        self.__arreglo[suc-1, xdia]=self.__arreglo[suc-1, xdia]+imp
    def mostrarArreglo(self):
        dias_semana = ["         ", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        print("      ".join(dias_semana))
        for i in range(5):
            print(f"Sucursal {i+1}", end="      ")
            for j in range(7):
                print(self.__arreglo[i, j], end="         ")
            print()
    def facSucursal(self):
        suc=int(input("Ingrese la sucursal\n"))
        acum=0
        for j in range(7):
            acum=acum+self.__arreglo[suc-1, j]
        print(f"El total facturado en la semana de la sucursal {suc} es: ${acum}")
    def facDia(self):
        max=0
        dia=input("Ingrese el dia de la semana\n")
        if dia=="lunes":
            xdia=0
        elif dia=="martes":
            xdia=1
        elif dia=="miercoles":
            xdia=2
        elif dia=="jueves":
            xdia=3
        elif dia=="viernes":
            xdia=4
        elif dia=="sabado":
            xdia=5
        elif dia=="domingo":
            xdia=6
        for i in range(5):
            if self.__arreglo[i, xdia]>max:
                max=self.__arreglo[i, xdia]
                aux=i
        print(f"La sucursal que mas facturó ese día es la sucursal {aux+1}")
    def menosFac(self):
        min=999999999999
        for i in range(5):
            acum=0
            for j in range(7):
                acum=acum+self.__arreglo[i, j]
            if acum<min:
                min=acum
                aux=i
        print(f"La sucursal que menos facturó en la semana es la sucursal {aux+1}")
    def facTotal(self):
        acum=0
        for i in range(5):
            for j in range(7):
                acum=acum+self.__arreglo[i, j]
        print(f"La facturacion total es de: ${acum}")