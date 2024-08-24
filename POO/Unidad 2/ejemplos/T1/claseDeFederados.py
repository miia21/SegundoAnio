class claseFederados:
    __apellido:str
    __nombre:str
    __dni:int
    __edad:int
    __club:str

    def __init__(self,apellido,nombre,dni,edad,club):
        self.__apellido=apellido
        self.__nombre=nombre
        self.__dni=dni
        self.__edad=edad
        self.__club=club
    
    def __str__(self):
        return f"Apellido:{self.__apellido}\nNombre:{self.__nombre}\nDNI:{self.__dni}\nEdad:{self.__edad}\nClub:{self.__club}\n"
    
    def getApellido(self):
        return self.__apellido
    
    def getNombre(self):
        return self.__nombre
    
    def getDNI(self):
        return self.__dni
    
    def getEdad(self):
        return self.__edad
    
    def getClub(self):
        return self.__club