from publicaciones import *
class disco(publicacion):
    __duracion=int
    __narrador=str

    def __init__(self,titulo,categoria,preciobase,duracion,narrador):
        super().__init__(titulo,categoria,preciobase)
        self.__duracion=duracion
        self.__narrador=narrador

    def getduracion(self):
        return self.__duracion
    def getnarrador(self):
        return self.__narrador
    def __str__(self):
        return f"Titulo: {super().gettitulo}, Categoria: {super().getcategoria}, Importe: {super().getprecio}"