from claseVehiculo import Vehiculo

class Autobuses(Vehiculo):
    __tipoServ: str
    __Turno: str
    def __init__(self,marca=0,modelo=0,Fabricacion=0,capacidad=0,numero=0,distancia=0,tarifaBase=0,tipoServ=0,Turno=0):
        super().__init__(marca,modelo,Fabricacion,capacidad,numero,distancia,tarifaBase)
        self.__tipoServ = tipoServ
        self.__Turno = Turno
    def getTipoServ(self):
        return self.__tipoServ
    def getTurno(self):
        return self.__Turno
    def getTarifa(self):
        tarifaTotal = 0
        cuenta = 0
        if self.getTipoServ().lower() == 'turismo' and self.getTurno().lower() == 'noche':
            tarifabase = super().getTarifaBase()
            cuenta = tarifabase * 0.2
            tarifaTotal = tarifabase + cuenta
            return tarifaTotal
        else:
            tarifabase = super().getTarifaBase()
            cuenta = tarifabase * 0.05
            tarifaTotal = tarifabase + cuenta
            return tarifaTotal