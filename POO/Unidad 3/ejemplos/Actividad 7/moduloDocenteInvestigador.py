import sys
sys.dont_write_bytecode = True
from moduloDocente import docente
from moduloInvestigador import investigador

class docenteInvestigador(docente, investigador):
   __aporteExtra: float
   __categoriaIncentivo : int
   
   def __init__(self, cuil, apellido, nombre, sueldoBasico, antiguedad,areaInvestigacion,tipoInvestigacion, aporteExtra, categoriaIncentivo, carrera, cargo, catedra):
      super().__init__(cuil, apellido, nombre, sueldoBasico, antiguedad, areaInvestigacion, tipoInvestigacion, carrera, cargo, catedra)
      self.__aporteExtra = aporteExtra
      self.__categoriaIncentivo = categoriaIncentivo
      
   
   def getAporteExtra(self):
      return self.__aporteExtra
   
   def getCategoriaIncentivo(self):
      return self.__categoriaIncentivo
   
   def getSueldo(self):
      return super().getSueldo() + self.__aporteExtra
   
   def toJSON(self):
      diccionario = dict(
      clase = __class__.__name__,   
      atributos = dict(
         cuil = super().getCuil(),
         nombre = super().getNombre(),
         apellido = super().getApellido(),
         sueldoBasico = super().getSueldoBasico(),
         antiguedad = super().getAntiguedad(),
         carrera = super().getCarrera(),
         cargo = super().getCargo(),
         catedra = super().getCatedra(),
         areaInvestigacion = super().getAreaInvestigacion(),
         tipoInvestigacion = super().getTipoInvestigacion(),
         aporteExtra = self.__aporteExtra,
         categoriaIncentivo = self.__categoriaIncentivo
      )
      )
      return diccionario