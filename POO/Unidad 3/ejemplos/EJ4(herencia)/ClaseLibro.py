from ClasePublicaciones import publicacion
from datetime import date
class Libro(publicacion):
    __nombreautor: str
    __fecha: str
    __cantpaginas: str
    def __init__(self, titulo, categoria, precio,nombrea,fecha,cantpaginas):
        self.__nombreautor=nombrea
        self.__fecha=fecha
        self.__cantpaginas=cantpaginas
        super().__init__(titulo, categoria, precio)
    def gettitulo(self):
        return super().gettitulo()
    def getprecio(self):
        return super().getprecio()
    def importetotal(self):
        lista=self.__fecha
        lista.split('/')
        today=date.today()
        año=today.year
        porcentaje=(super().getprecio()*(año-int(lista[0])))/100
        total=float(super().getprecio()-porcentaje)
        return total