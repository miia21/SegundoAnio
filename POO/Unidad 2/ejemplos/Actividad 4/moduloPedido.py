class pedido:
   __patente: str
   __id : str
   __comidasPedidas: str
   __tiempoDeEntrega : int
   __tiempoReal: int
   __precio : float
   def __init__(self, patente, identificador, comidas, tiempoEntrega, precio):
      self.__patente = patente
      self.__id = int(identificador)
      self.__comidasPedidas = comidas
      self.__tiempoDeEntrega = tiempoEntrega
      self.__tiempoReal = 0
      self.__precio = precio
      int(self.__tiempoDeEntrega)
      float(self.__precio)
  
  
   def mostrarDatos(self):
      #print(f"""El pedido {self.__id} que contiene: {self.__comidasPedidas} por el vehiculo {self.__patente}
      #     Con precio: {self.__precio} y tiempo estimado de: {self.__tiempoDeEntrega} segundos""")
      minutosReal = int(self.__tiempoReal / 60)
      segundosReal = int(self.__tiempoReal % 60)
      print(f"Patente: {self.__patente}, id:{self.__id} y tiempo real: {minutosReal}:{segundosReal}")
  
  
   def getPatente(self):
      return self.__patente
   
   
   def getID(self):
      return self.__id
   
   
   def getTiempoReal(self):
      return self.__tiempoReal
   
   
   def getTiempoEstimado(self):
      return self.__tiempoDeEntrega
   
   
   def getPrecio(self):
      return self.__precio
   
   
   def __lt__(self, otro):
      return (self.__patente < otro.getPatente())
   
   
   def setTiempoReal(self, tiempo):
      self.__tiempoReal = tiempo