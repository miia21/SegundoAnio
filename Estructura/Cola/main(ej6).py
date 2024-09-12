from colaEnlazada import colaE

class trabajo:
    __horas: int
    __salario: int

    def __init__(self, nombre, horas, salario):
        self.__nombre = nombre
        self.__horas = horas
        self.__salario = salario

if __name__ == "__main__":
    cola = colaE()
    