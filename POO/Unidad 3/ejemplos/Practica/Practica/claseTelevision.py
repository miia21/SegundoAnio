from clasePlanes import Planes
class Television(Planes):
    __nacionales:int
    __internacionales:int
    def __init__(self, nombComp=0, duracion=0, cobertura=0, precioBase=0,**kwargs):
        super().__init__(nombComp, duracion, cobertura, precioBase)
        self.__nacionales = kwargs['nacionales']
        self.__internacionales = kwargs['internacionales']
    def getNacionales(self):
        return int(self.__nacionales)
    def getInternacionales(self):
        return int(self.__internacionales)
    def precio(self):
        if self.getInternacionales() > 10:
            return self.getPrecioBase() + (self.getPrecioBase() * 0.15)
        else:
            return self.getPrecioBase()
    
        