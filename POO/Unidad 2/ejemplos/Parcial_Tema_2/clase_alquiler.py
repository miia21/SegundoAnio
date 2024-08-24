class alquiler:
    __persona:str
    __id:str
    __hora:int
    __minutos:int
    __duracion:int
    def __init__(self,p,i,h,m,d):
        self.__persona=p
        self.__id=i
        self.__hora=h
        self.__minutos=m
        self.__duracion=int(d)
    
    def __gt__(self, other):
        return (self.__hora + self.__minutos) > (other.__hora + other.__minutos)
    def get_id(self):
        return self.__id
    def get_hora(self):
        return self.__hora
    def get_min(self):
        return self.__minutos
    def get_dura(self):
        return self.__duracion