from claseVehiculo import Vehiculo
class Vanes(Vehiculo):
    __tipoCarro: str
    def __init__(self,marca=0,modelo=0,Fabricacion=0,capacidad=0,numero=0,distancia=0,tarifaBase=0,tipoCarro=0):
        super().__init__(marca,modelo,Fabricacion,capacidad,numero,distancia,tarifaBase)
        self.__tipoCarro = tipoCarro
    def getTipoCarro(self):
        return self.__tipoCarro
    def getTarifa(self):
        tarifaTotal = 0
        cuenta = 0
        if self.getTipoCarro().lower() == 'minivan':

            cuenta = super().getTarifaBase() * 0.1
            tarifaTotal = super().getTarifaBase() - cuenta
            return tarifaTotal
        else:
            cuenta = super().getTarifaBase() * 0.025
            tarifaTotal = super().getTarifaBase() + cuenta
            return tarifaTotal