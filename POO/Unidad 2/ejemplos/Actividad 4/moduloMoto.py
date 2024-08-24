class moto:
   __patente : str
   __marca : str
   __nombreConductor : str
   __kilometraje : int
   def __init__(self, patente, marca, nombre, km):
      self.__patente = patente
      self.__marca = marca
      self.__nombreConductor = nombre
      self.__kilometraje = km
      int(self.__kilometraje)
      
      
   def getPatente(self):
      return self.__patente
   
   
   def getNyA(self):
      return self.__nombreConductor
   
   
   def getKm(self):
      return self.__kilometraje
   
   
   def getMarca(self):
      return self.__marca
   
   
   def __lt__(self, otro):
      return (self.__patente < otro.getPatente())
   