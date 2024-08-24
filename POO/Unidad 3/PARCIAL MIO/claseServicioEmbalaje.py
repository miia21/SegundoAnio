from claseServicio import servicio

class servicioEmbalaje(servicio):
    __precioUnidad: float
    __peso: float
    __cant: int
    def __init__(self, nom1, nom2, dir, fe, com, **kwargs):
        super().__init__(nom1, nom2, dir, fe, com)
        self.__precioUnidad=kwargs['precio']
        self.__peso=kwargs['peso']
        self.__cant=kwargs['cantidad']
    def costoTotal(self):
        costo=self.__precioUnidad*self.__cant
        if self.__peso>50:
            costo+=costo*0.1
        costo+=self.getCom()
        return costo
    def getPeso(self):
        return self.__peso