from listaEnlazadaOrdenada import listaE

class matriz:
    __fila: int
    __columna: int
    __valor: int

    def __init__(self, fila, columna, valor):
        self.__fila = fila
        self.__columna = columna
        self.__valor = valor

    def getFila(self):
        return self.__fila

    def getColumna(self):
        return self.__columna

    def getValor(self):
        return self.__valor
    
    def __lt__(self, otro):
      if self.__fila < otro.getFila() and self.__columna < otro.getColumna():
         return True
      else:
         return False
   
    def __eq__(self, otro):
        if self.__fila == otro.getFila() and self.__columna == otro.getColumna():
            return True
        else:
            return False
    
    def __le__(self, otro):
        filaOtro = otro.getFila()
        columnaOtro = otro.getColumna()
        if self.__fila < filaOtro:
            return True
        elif self.__fila == filaOtro:
            if self.__columna <= columnaOtro:
                return True
            else:
                return False
        else:
            return False
    
    def __str__(self):
        return f"({self.__fila}, {self.__columna}, {self.__valor})"

if __name__ == "__main__":
    lista1 = listaE()
    lista1.insertar(matriz(1, 1, 5))
    lista1.insertar(matriz(2, 3, 2))
    lista1.insertar(matriz(6, 5, 3))
    lista1.insertar(matriz(6, 6, 4))

    lista2 = listaE()
    lista2.insertar(matriz(1, 1, 5))
    lista2.insertar(matriz(4, 3, 2))
    lista2.insertar(matriz(6, 5, 4))
    lista2.insertar(matriz(6, 6, 4))

    matrizSuma = listaE()
   
    i = 1
    j = 1
   
    while i < lista1.getCant() and j < lista2.getCant():
        elemento1 = lista1.recuperar(i)
        elemento2 = lista2.recuperar(j)
        if elemento1 == elemento2:
            matrizSuma.insertar(matriz(elemento1.getFila(), elemento1.getColumna(), elemento1.getValor() + elemento2.getValor()))
            i += 1
            j += 1
        elif elemento1 < elemento2:
            matrizSuma.insertar(elemento1)
            i += 1
        else:
            matrizSuma.insertar(elemento2)
            j += 1
    
    while i <= lista1.getCant():
        elemento1 = lista1.recuperar(i)
        matrizSuma.insertar(elemento1)
        i += 1
    
    while j <= lista2.getCant():
        elemento2 = lista2.recuperar(j)
        matrizSuma.insertar(elemento2)
        j += 1
    
    
    print("El resultado de la matriz suma es: ")
    matrizSuma.mostrar()