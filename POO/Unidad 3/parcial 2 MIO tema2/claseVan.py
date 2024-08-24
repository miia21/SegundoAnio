from claseVehiculo import vehiculo

class van(vehiculo):
    __tipo: str
    def __init__(self, marca, modelo, anio, capacidad, num, dis, tari, **kwargs):
        super().__init__(marca, modelo, anio, capacidad, num, dis, tari)
        self.__tipo=kwargs['tipo']
    def tarifa(self):
        x=0
        if self.__tipo=='minivan':
            x=self.getTarifa()-(self.getTarifa()*0.1)
        else:
            x=self.getTarifa()+(self.getTarifa()*0.025)
        return x
    