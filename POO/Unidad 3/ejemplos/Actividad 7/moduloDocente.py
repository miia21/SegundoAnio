import sys
sys.dont_write_bytecode = True
from moduloPersonal import personal
class docente(personal):
   __carrera : str
   __cargo : str
   __catedra : str
   
   def __init__(self, cuil, apellido, nombre, sueldoBasico, antiguedad, areaInvestigacion = None, tipoInvestigacion = None, carrera = None, cargo = "", catedra = None):
      super().__init__(cuil, apellido, nombre, sueldoBasico, antiguedad, carrera, cargo, catedra, areaInvestigacion, tipoInvestigacion)
      self.__carrera = carrera
      self.__cargo = cargo
      self.__catedra = catedra
   
   
   def getCarrera(self):
      return self.__carrera
   
   def getCargo(self):
      return self.__cargo
   
   def getCatedra(self):
      return self.__catedra
   
   def getSueldo(self):
      sueldoBase = super().getSueldoBasico()
      antiguedad = sueldoBase * ((super().getAntiguedad()/100))
      cargoAux = self.__cargo.lower()
      if cargoAux == "simple":
         cargo = sueldoBase * 0.1
      elif cargoAux == "semiexclusivo":
         cargo = sueldoBase * 0.2
      elif cargoAux == "exclusivo":
         cargo = sueldoBase * 0.5
      else:
         cargo = 0
      sueldo = sueldoBase + antiguedad + cargo
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
         carrera = self.__carrera,
         cargo = self.__cargo,
         catedra = self.__catedra
      )
      )
      return diccionario   