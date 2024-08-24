from ProdRefrigerado import ProdRefrigerado
from ProdCongelado import ProdCongelado
from GestorProductos import GestorProductos
from os import path

def menu():
    op=int(input("""
                            Menú de Opciones
            [1] Agregar producto
            [2] Conocer tipo de producto a partir de su posicion
            [3] Mostrar cantidad de productos de cada tipo
            [4] Mostrar datos de las productos (Nombre, pais, temperatura de mantenimiento y precio base)
            [0] SALIR
            -> """))
    return op

if __name__ == "__main__":
    MP = GestorProductos()
    MP.cargar(path.dirname(__file__) + "/productos.csv")
    #print(MP)

    opcion = menu()
    while opcion != 0:
        if opcion==1:
            tipoOp1=int(input('Tipo: [1] Producto Refrigerado [2] Producto Congelado [0] Cancelar\n -> '))

            while (tipoOp1 in (1,2,0)) is False: #Si la opcion no es ninguna de las presentadas en el print anterior.
                tipoOp1=int(input('Tipo invalido. [1] Libro Impreso [2] Audio-Libro [0] Cancelar\n -> '))

            if tipoOp1!= 0:
                nomOp1=input('Ingrese nombre de producto: ')
                fechaEOp1=input('Fecha de Envasado: ')
                fechaVOp1=input('Fecha de Vencimiento: ')
                tempMantOp1=input('Temperatura de Mantenimiento: ')
                paisOp1=input('Pais: ')
                loteOp1=input('Numero de Lote: ')
                costoBOp1=float(input('Costo Base: '))

                if tipoOp1 == 1:
                    codOrgOp1=input('Codigo de organismo de supervision alimentaria: ')
                    nuevoProducto=ProdRefrigerado(nombre=nomOp1,fechaE=fechaEOp1,fechaV=fechaVOp1,tempMant=tempMantOp1,pais=paisOp1,lote=loteOp1, costoB=costoBOp1, codOrg=codOrgOp1)
                else:
                    nitroOp1=int(input('Nitrogeno (a pesar de ser un porcentaje ingrese solo valor entero): '))
                    oxiOp1=input('Oxigeno (a pesar de ser un porcentaje ingrese solo valor entero): ')
                    dioxiOp1=input('Dioxido de carbono (a pesar de ser un porcentaje ingrese solo valor entero): ')
                    vaporOp1=input('Vapor (a pesar de ser un porcentaje ingrese solo valor entero): ')
                    metodoOp1=input('Metodo (solo ingrese "mecanico" o "criogenico"): ')
                    nuevoProducto=ProdCongelado(nombre=nomOp1,fechaE=fechaEOp1,fechaV=fechaVOp1,tempMant=tempMantOp1,pais=paisOp1,lote=loteOp1, costoB=costoBOp1, nitro=nitroOp1, oxi=oxiOp1, dioxido=dioxiOp1, vapor=vaporOp1, metodo=metodoOp1)
                MP.agregarProducto(nuevoProducto)

        if opcion == 2:
            posicion = int(input("Ingrese la posicion a buscar: "))
            MP.getTipoProducto(posicion)

        if opcion == 3:
            MP.mostrarCantidadTipo()

        if opcion == 4:
            print(MP)

