import csv
from ProdRefrigerado import ProdRefrigerado
from ProdCongelado import ProdCongelado

class GestorProductos:
    __Productos: list

    def __init__(self):
        self.__Productos = []

    def agregarProducto(self, prod):
        self.__Productos.append(prod)
    

    def cargar(self, ruta):
        archi = open(ruta)
        reader = csv.reader(archi, delimiter=";")
        band = True
        for fila in reader:
            if band:
                band = not band
            else:
                if fila[0] == 'R':
                    prod = ProdRefrigerado(nombre=fila[1],fechaE=fila[2],fechaV=fila[3],tempMant=fila[4],pais=fila[5],lote=fila[6],costoB=float(fila[7]),codOrg=fila[8])
                if fila[0] == 'C':
                    prod = ProdCongelado(nombre=fila[1],fechaE=fila[2],fechaV=fila[3],tempMant=fila[4],pais=fila[5],lote=fila[6],costoB=float(fila[7]),nitro=int(fila[8]),oxi=int(fila[9]),dioxido=int(fila[10]),vapor=int(fila[11]),metodo=fila[12])
                self.agregarProducto(prod)

    def __str__(self):
        s = ""
        for prod in self.__Productos:
            s += str(prod) + "\n"
        return s
    
    def getTipoProducto(self,pos):
        if pos < len(self.__Productos):
            if isinstance(self.__Productos[pos], ProdRefrigerado):
                print(f"El producto en la posicion {pos} es uno refigerado")
            if isinstance(self.__Productos[pos], ProdCongelado):
                print(f"El producto en la poscion {pos} es uno congelado")
        else:
            print(f'Indice invalido. Solo puede variar entre 0 y {len(self.__Productos)}')

    def mostrarCantidadTipo(self):
        refrigerados=0
        congelados=0
        for producto in self.__Productos:
            if isinstance(producto,ProdRefrigerado):
                refrigerados+=1
            elif isinstance(producto,ProdCongelado):
                congelados+=1
        print(f"Hay {refrigerados} productos refrigerados Y {congelados} productos congelados")
        return

    