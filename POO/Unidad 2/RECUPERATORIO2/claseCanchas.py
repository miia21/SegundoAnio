class cancha:
    __id: str
    __tipo: str
    __imp: float
    def __init__(self, id, t, imp):
        self.__id=id
        self.__tipo=t
        self.__imp=imp
    def getId(self):
        return self.__id
    def getImp(self):
        return self.__imp
    