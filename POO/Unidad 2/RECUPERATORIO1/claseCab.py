class cab:
    __num: int
    __canth: int
    __cantcg: int
    __cantcc: int
    __imp: float
    def __init__(self, n, ch, cg, cc, i):
        self.__num=n
        self.__canth=ch
        self.__cantcg=cg
        self.__cantcc=cc
        self.__imp=i
    def getNum(self):
        return self.__num
    def getImp(self):
        return self.__imp
    def __ge__(self, otro):
        return ((self.__cantcg * 2) + self.__cantcc)>=otro