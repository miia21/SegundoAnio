from claseVehiculo import vehiculo

class autobus(vehiculo):
    __tipo: str
    __turno: str
    def __init__(self, marca, modelo, anio, capacidad, num, dis, tari, **kwargs):
        super().__init__(marca, modelo, anio, capacidad, num, dis, tari)
        self.__tipo=kwargs['tipo']
        self.__turno=kwargs['turno']
    def tarifa(self):
        x=0
        if self.__tipo=='turismo' and self.__turno=='noche':
            x=self.getTarifa()+(self.getTarifa()*0.2)
        else:
            x=self.getTarifa()+(self.getTarifa()*0.05)
        return x
    