class nodo:
   __sig : object
   __datos : object
   
   def __init__(self, sig, datos):
      self.__sig = sig
      self.__datos = datos
      
   
   def datos(self):
      return self.__datos
   
   def sig(self):
      return self.__sig
   
   def setSig(self, nodo):
      self.__sig = nodo
   
   def __str__(self):
      return self.datos.__str__()
   
   def toJSON(self):
      return self.datos.toJSON()
   
   def getTipo(self):
      return type(self.__datos)
   
   def __lt__(self, otro):
      return self.datos.__lt__(otro)