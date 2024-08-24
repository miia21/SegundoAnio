from Ej1.claseCajaAhorro import cajaAhorro
from claseLista import lista

if __name__ == '__main__':
    lista = lista()
    caja1=cajaAhorro(123, "27-45800361-6", "Pastor", "Mia", 5000)
    caja2=cajaAhorro(321, "20-34566234-3", "Savall", "Alejo", 4000)
    lista.agregar_caja(caja1)
    lista.agregar_caja(caja2)
    cuil=input("Ingrese un cuil a buscar\n")
    lista.obtenerDatos(cuil)