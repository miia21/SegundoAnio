import sys
sys.dont_write_bytecode = True
from moduloPersonal import personal
class personalApoyo(personal):
   __categoria: int
   __porcentaje : float
   
   def __init__(self, cuil, apellido, nombre, sueldoBasico, antiguedad, categoria, porcentaje = -1):
      super().__init__(cuil, apellido, nombre, sueldoBasico, antiguedad)
      self.__categoria = categoria
      self.__porcentaje = porcentaje
   
   def getCategoria(self):
      return self.__categoria
   
   def setPorcentajeCategoria(self, nuevoPorcentaje):
      self.__porcentaje = nuevoPorcentaje
   
   def getSueldo(self):
      sueldoBase = super().getSueldoBasico()
      antiguedad = sueldoBase * ((super().getAntiguedad()/100))
      if self.__porcentaje	== -1:
         if(self.__categoria in range(1,11)):
            categoria = sueldoBase * 0.1
         elif(self.__categoria in range(11, 21)):
            categoria = sueldoBase * 0.2
         else:
            categoria = sueldoBase * 0.3
      else:
         categoria = sueldoBase * self.__porcentaje
      sueldo = sueldoBase + antiguedad + categoria
      return sueldo
   
   def toJSON(self):
      diccionario = dict(
      clase = __class__.__name__,
      atributos = dict(
         cuil = super().getCuil(),
         nombre = super().getNombre(),
         apellido = super().getApellido(),
         sueldoBasico = super().getSueldoBasico(),
         antiguedad = super().getAntiguedad(),
         categoria = self.__categoria,
         porcentaje = self.__porcentaje
      )
      )
      return diccionario   
      
      