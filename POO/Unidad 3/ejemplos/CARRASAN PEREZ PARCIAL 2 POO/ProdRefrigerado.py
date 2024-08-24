from Producto import Producto
import datetime

class ProdRefrigerado(Producto):
    __codOrg: int

    def __init__(self, **kwargs):
        super().__init__(kwargs['nombre'], kwargs['fechaE'], kwargs['fechaV'], kwargs['tempMant'], kwargs['pais'], kwargs['lote'], kwargs['costoB'])
        self.__codOrg = kwargs['codOrg']

    def getCodOrg(self):
        return self.__codOrg
    
    def getImporteVenta(self):
        fechaV = self.getFechaV()
        fechaV = int(fechaV.split('/')[1])
        fechaH = datetime.date.today()
        if fechaV - fechaH.month <= 2:
            importe = float(self.getCostoBase()) - (float(self.getCostoBase()*0.1))
        else:
            importe = float(self.getCostoBase()) + (float(self.getCostoBase())*0.01)
        return importe
    
    def __str__(self):
        return f'Nombre: {super().getNombre()}\n  Pais: {super().getPais()} Temperatura de Mantenimiento: {super().getTempMant()} Precio de Venta: {self.getImporteVenta()}'