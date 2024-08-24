import sys
sys.dont_write_bytecode = True
from moduloPersonal import personal

class investigador(personal):
   __areaInvestigacion : str
   __tipoInvestigacion: str
   
   def __init__(self, cuil, apellido, nombre, sueldoBasico, antiguedad, areaInvestigacion = None, tipoInvestigacion = None, carrera = None, cargo = None, catedra = None):
      super().__init__(cuil, apellido, nombre, sueldoBasico, antiguedad, areaInvestigacion, tipoInvestigacion, carrera, cargo, catedra)
      self.__areaInvestigacion = areaInvestigacion
      self.__tipoInvestigacion = tipoInvestigacion
      
   def getAreaInvestigacion(self):
      return self.__areaInvestigacion
   
   def getTipoInvestigacion(self):
      return self.__tipoInvestigacion
   
   def getSueldo(self):
      sueldoBase = super().getSueldoBasico()
      antiguedad = sueldoBase * ((super().getAntiguedad()/100))
      sueldo = sueldoBase + antiguedad
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
         areaInvestigacion = self.__areaInvestigacion,
         tipoInvestigacion = self.__tipoInvestigacion
      )
      )
      return diccionario