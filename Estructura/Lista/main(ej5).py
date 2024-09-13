from listaEnlazadaOrdenada import listaE

class Termino:
    __coeficiente: int
    __grado: int

    def __init__(self, coeficiente: int, grado: int):
        self.__coeficiente = coeficiente
        self.__grado = grado

    def setGrado(self, grado: int) -> None:
        self.__grado = grado

    def setCoeficiente(self, coeficiente: int) -> None:
        self.__coeficiente = coeficiente

    def getGrado(self) -> int:
        return self.__grado

    def getCoeficiente(self) -> int:
        return self.__coeficiente

    def __str__(self) -> str:
        return str(self.__coeficiente) + "x^" + str(self.__grado)

    def __eq__(self, otro: object) -> bool:
        if isinstance(otro, Termino):
            return self.__grado == otro.getGrado()
        return False

    def __gt__(self, otro: object) -> bool:
        if isinstance(otro, Termino):
            return self.__grado > otro.getGrado()
        return False

    def __ge__(self, otro: object) -> bool:
        if isinstance(otro, Termino):
            return self.__grado >= otro.getGrado()
        return False

def buscar_termino(polinomio, grado):
    i = 1
    while i <= polinomio.getCant():
        termino = polinomio.recuperar(i)
        if termino.getGrado() == grado:
            return termino
        i += 1
    return None

def sumarPolinomios(polinomio1, polinomio2):
    polinomioResultado = listaE()

    # Sumar términos del primer polinomio
    i = 1
    while i <= polinomio1.getCant():
        termino1 = polinomio1.recuperar(i)
        termino2 = buscar_termino(polinomio2, termino1.getGrado())
        
        if termino2:
            nuevoCoeficiente = termino1.getCoeficiente() + termino2.getCoeficiente()
            if nuevoCoeficiente != 0:  # No agregar términos con coeficiente 0
                polinomioResultado.insertar(Termino(nuevoCoeficiente, termino1.getGrado()))
        else:
            polinomioResultado.insertar(termino1)
        i += 1

    # Agregar términos restantes del segundo polinomio que no fueron sumados
    grados_sumados = {termino1.getGrado() for i in range(1, polinomio1.getCant() + 1)
                      for termino1 in [polinomio1.recuperar(i)]}
    
    i = 1
    while i <= polinomio2.getCant():
        termino2 = polinomio2.recuperar(i)
        if termino2.getGrado() not in grados_sumados:
            polinomioResultado.insertar(termino2)
        i += 1

    return polinomioResultado

if __name__ == "__main__":
    polinomio1 = listaE()
    polinomio2 = listaE()

    # Termino(coeficiente, grado)
    polinomio1.insertar(Termino(3, 2))
    polinomio1.insertar(Termino(4, 1))
    polinomio1.insertar(Termino(2, 0))

    polinomio2.insertar(Termino(5, 4))
    polinomio2.insertar(Termino(2, 3))
    polinomio2.insertar(Termino(1, 2))
    polinomio2.insertar(Termino(3, 0))

    polinomioSuma = sumarPolinomios(polinomio1, polinomio2)

    print("La suma de los polinomios da como resultado:")
    polinomioSuma.mostrar()
