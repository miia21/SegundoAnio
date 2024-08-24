from clase_servicio import Servicio

class Transporte(Servicio):
    __precio:float
    __peso:float
    __direccion_destino:str
    __cantidad:int
    def __init__(self,nombre,contratante,direccion,fecha,comision,precio,peso,direccion_destino,cantidad):
        super().__init__(nombre,contratante,direccion,fecha,comision)
        self.__precio=precio
        self.__peso=peso
        self.__direccion_destino=direccion_destino
        self.__cantidad=cantidad
    def __str__(self):
        texto="{}\t\t{}"
        return texto.format(super().contratante,self.costo_total())
    def costo_total(self):
        costo=super().comision
        if self.peso > 500:
            costo += self.__precio * self.cantidad* + (super().comision * 0.10)
        return costo
    @property
    def cantidad(self):
        return self.__cantidad
    @property
    def precio(self):
        return self.__precio
    @property
    def peso(self):
        return self.__peso
    @property
    def direccion_destino(self):
        return self.__direccion_destino
    def __lt__(self,other):
        return self.costo_total() < other.costo_total()