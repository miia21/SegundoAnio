from claseServicio import servicio

class servicioTransporte(servicio):
    __precioHora: float
    __peso: float
    __cant: int
    __direcDes: str
    def __init__(self, nom1, nom2, dir, fe, com, **kwargs):
        super().__init__(nom1, nom2, dir, fe, com)
        self.__precioHora=kwargs['precio']
        self.__peso=kwargs['peso']
        self.__cant=kwargs['cantidad']
        self.__direcDes=kwargs['direccion']
    def costoTotal(self):
        costo=self.__precioHora*self.__cant
        if self.__peso>500:
            costo+=costo*0.1
        costo+=self.getCom()
        return costo
    def __lt__(self, otro):
        return self.costoTotal()<otro.costoTotal()
    
