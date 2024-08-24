from Producto import Producto

class ProdCongelado(Producto):
    __nitrogeno = int
    __oxigeno = int
    __dioxido = int
    __vapor = int
    __metodo = str

    def __init__(self, **kwargs):
        super().__init__(kwargs['nombre'], kwargs['fechaE'], kwargs['fechaV'], kwargs['tempMant'], kwargs['pais'], kwargs['lote'], kwargs['costoB'])
        self.__nitrogeno = kwargs['nitro']
        self.__oxigeno = kwargs['oxi']
        self.__dioxido = kwargs['dioxido']
        self.__vapor = kwargs['vapor']
        self.__metodo = kwargs['metodo']

    def getNitro(self):
        return self.__nitrogeno
    
    def getOxi(self):
        return self.__oxigeno
    
    def getDioxi(self):
        return self.__dioxido
    
    def getVapor(self):
        return self.__vapor
    
    def getMetodo(self):
        return self.__metodo
    
    def getImporteVenta(self):
        if self.getMetodo().strip().lower() == 'mecanico':
            importe = self.getCostoBase() * 1.15
        if self.getMetodo() == 'criogenico':
            importe = self.getCostoBase() * 1.15

        return importe
    
    def __str__(self):
        return f'Nombre: {super().getNombre()}\n  Pais: {super().getPais()} Temperatura de Mantenimiento: {super().getTempMant()} Precio de Venta: {self.getImporteVenta()}'

