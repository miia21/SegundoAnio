from clasePlanes import Planes
class Telefonia(Planes):
    __tipoLlamada:str
    __cantMinutos:str
    def __init__(self, nombComp=0, duracion=0, cobertura=0, precioBase=0,**kwargs):
        super().__init__(nombComp, duracion, cobertura, precioBase)
        self.__tipoLlamada = kwargs['tipoLlamada']
        self.__cantMinutos = kwargs['cantMinutos']
    def getTipoLlamada(self):
        return self.__tipoLlamada
    def getCantMinutos(self):
        return self.__cantMinutos
    def precio(self):
        cuenta = 0
        if self.getTipoLlamada().lower() == 'internacional':
            cuenta = self.getPrecioBase() + (self.getPrecioBase() * 0.20)
            return cuenta
        elif self.getTipoLlamada().lower() == 'locales':
            cuenta = self.getPrecioBase() - (self.getPrecioBase() * 0.075)
            return cuenta
        else:
            return self.getPrecioBase()