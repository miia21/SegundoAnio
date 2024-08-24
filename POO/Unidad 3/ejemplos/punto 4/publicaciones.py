class publicacion:
    __titulo=str
    __categoria=str
    __preciobase=float

    def __init__(self,titulo,categoria,preciobase):
        self.__titulo=titulo
        self.__categoria=categoria
        self.__preciobase=preciobase

    def gettitulo(self):
        return self.__titulo
    def getcategoria(self):
        return self.__categoria
    def getprecio(self):
        return self.__preciobase
    """
    def __str__(self):
        return f"Titulo: {self.gettitulo}, Categoria: {self.getcategoria}, Importe: {self.getprecio}"
        """