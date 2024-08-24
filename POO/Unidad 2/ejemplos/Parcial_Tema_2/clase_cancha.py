class cancha:
    __id:str
    __piso:str
    __importe:float
    def __init__(self,ide,piso,imp):
        self.__id=ide
        self.__piso=piso
        self.__importe=float(imp)
    def get_imp(self):
        return self.__importe
    def get_id(self):
        return self.__id
