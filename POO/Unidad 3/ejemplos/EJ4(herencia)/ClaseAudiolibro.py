from ClasePublicaciones import publicacion
class audiolibro(publicacion):
    __nombreNarrador: str
    __duracion: int
    def __init__(self, titulo, categoria, precio,nombrenarrador,duracion):
        super().__init__(titulo, categoria, precio)
        self.__nombreNarrador=nombrenarrador
        self.__duracion=duracion
    def gettitulo(self):
        return super().gettitulo()
    def getprecio(self):
        return super().getprecio()
    def getduracion(self):
        return self.__duracion