class publicacion:
    __titulo: str
    __categoria: str
    __preciobase: float
    def __init__(self,titulo,categoria,precio):
        self.__titulo=titulo
        self.__categoria=categoria
        self.__preciobase=precio
    def gettitulo(self):
        return self.__titulo
    def getprecio(self):
        return self.__preciobase
    def getcategoria(self):
        return self.__categoria