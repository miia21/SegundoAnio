class servicio():
    __nomEmpresa: str
    __nomContra: str
    __dire: str
    __fecha: str
    __comision: float
    def __init__(self, nom1, nom2, dir, fe, com):
        self.__nomEmpresa=nom1
        self.__nomContra=nom2
        self.__dire=dir
        self.__fecha=fe
        self.__comision=com
    def getNomEmp(self):
        return self.__nomEmpresa
    def getNomCont(self):
        return self.__nomContra
    def getDir(self):
        return self.__dire
    def getFecha(self):
        return self.__fecha
    def getCom(self):
        return self.__comision