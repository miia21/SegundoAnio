from publicaciones import *
class libro(publicacion):
    __autor=str
    __edicion=str
    __paginas=int

    def __init__(self,titulo,categoria,preciobase,autor,edicion,paginas):
        super().__init__(titulo,categoria,preciobase)
        self.__autor=autor
        self.__edicion=edicion
        self.__paginas=paginas

    def getautor(self):
        return self.__autor
    def getadicion(self):
        return self.__edicion
    def getpaginas(self):
        return self.__paginas
    def __str__(self):
        return f"Titulo: {super().gettitulo}, Categoria: {super().getcategoria}, Importe: {super().getprecio}"