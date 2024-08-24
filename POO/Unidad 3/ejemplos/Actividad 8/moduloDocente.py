import sys
sys.dont_write_bytecode = True
from moduloPersonal import personal
class docente(personal):
   __carrera : str
   __cargo : str
   __catedra : str
   __porcentaje : float
   
   def __init__(self, cuil, apellido, nombre, sueldoBasico, antiguedad, areaInvestigacion = None, tipoInvestigacion = None, carrera = None, cargo = "", catedra = None, porcentaje = -1):
      super().__init__(cuil, apellido, nombre, sueldoBasico, antiguedad, carrera, cargo, catedra, areaInvestigacion, tipoInvestigacion)
      self.__carrera = carrera
      self.__cargo = cargo
      self.__catedra = catedra
      self.__porcentaje = porcentaje
   
   
   def getCarrera(self):
      return self.__carrera
   
   def getCargo(self):
      return self.__cargo
   
   def getCatedra(self):
      return self.__catedra

   def setPorcentajeCargo(self, nuevoPorcentaje):
      self.__porcentaje = nuevoPorcentaje
      
   def getPorcentaje(self):
      return self.__porcentaje
   
   def getSueldo(self):
      sueldoBase = super().getSueldoBasico()
      antiguedad = sueldoBase * ((super().getAntiguedad()/100))
      cargoAux = self.__cargo.lower()
      if self.__porcentaje == -1:
         if cargoAux == "simple":
            cargo = sueldoBase * 0.1
         elif cargoAux == "semiexclusivo":
            cargo = sueldoBase * 0.2
         elif cargoAux == "exclusivo":
            cargo = sueldoBase * 0.5
         else:
            cargo = 0
      else:
         cargo = sueldoBase * self.__porcentaje
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
         catedra = self.__catedra,
         porcentaje = self.__porcentaje
      )
      )
      return diccionario   