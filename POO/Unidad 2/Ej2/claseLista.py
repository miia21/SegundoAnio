from Ej1.claseCajaAhorro import cajaAhorro

class lista:
    __cajas: list
    def __init__(self):
        self.__cajas=[]
    def agregar_caja(self, caja):
        self.__cajas.append(caja)
    def mostrar_cajas(self):
        for cajaAhorro in self.__cajas:
            cajaAhorro.mostrarDatos()
    def obtenerDatos(self, cuil):
        i=0
        encontrado=False
        for cajaAhorro in self.__cajas:
            if cuil!=self.__cajas[i].getCuil():
                i=+1
            else:
                encontrado=True
        if encontrado==True:
            x=self.__cajas[i]
            x.mostrarDatos()
        else:
            print("No se encontro el cuil\n")
        # while encontrado==False:
        #     if cuil == self.__cajas[i].getCuil():
        #         encontrado=True
        #         self.__cajas[i].mostrarDatos()
        #     else:
        #         i=i+1

