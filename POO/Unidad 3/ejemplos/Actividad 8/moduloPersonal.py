class personal:
   __cuil : str
   __apellido : str
   __nombre : str
   __sueldoBasico : float
   __antiguedad : int
   
   
   def __init__(self, cuil, apellido, nombre, sueldoBasico, antiguedad, carrera = None, cargo = None, catedra = None, areaInvestigacion = None, tipoInvestigacion = None):
      self.__cuil = cuil
      self.__apellido = apellido
      self.__nombre = nombre
      self.__sueldoBasico = sueldoBasico
      self.__antiguedad = antiguedad
      
   
   def getCuil(self):
      return self.__cuil
   
   def getApellido(self):
      return self.__apellido
   
   def getNombre(self):
      return self.__nombre
   
   def getSueldoBasico(self):
      return self.__sueldoBasico
   
   def getSueldo(self):
      return self.__sueldoBasico
  
   def getAntiguedad(self):
      return self.__antiguedad
   
   def setSueldoBasico(self, nuevoBasico):
      self.__sueldoBasico = nuevoBasico
   
   def __str__(self):
      return self.__nombre + " " + self.__apellido
   
   def __lt__(self, otro):
      return self.__nombre < otro.getNombre()
   
   def menorQue(self, otro):
      return self.__apellido < otro.getApellido()
   
   def toJSON(self):
      diccionario = dict(
      clase = __class__.__name__, 
      atributos = dict(
         cuil = self.__cuil,
         nombre = self.getNombre(),
         apellido = self.getApellido(),
         sueldoBasico = self.getSueldoBasico(),
         antiguedad = self.getAntiguedad()
      )
      )
      return diccionario   