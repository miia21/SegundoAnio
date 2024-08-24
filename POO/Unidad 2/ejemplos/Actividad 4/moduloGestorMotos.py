from moduloMoto import moto
from moduloGestorPedidos import gestorPedidos
import csv
class gestorMotos:
   __motos = []
  
  
   def __init__(self):
      archivoMotos = open('datosMotos.csv')
      reader = csv.reader(archivoMotos, delimiter=';')
      bandera = False 
      for fila in reader:
         if bandera == False:
            bandera = True
         else:
            objeto = moto(fila[0], fila[1], fila[2], fila[3])
            self.__motos.append(objeto)
      archivoMotos.close()
  
  
   def mostrarDatos(self, patenteIngresada):
      self.__motos.sort()
      piso = 0
      techo = len(self.__motos) -1
      medio = 0
      patente = self.__motos[medio].getPatente()
      while((piso < techo) and (patenteIngresada != patente)):
         medio = int((techo - piso) / 2)
         if patente < patenteIngresada:
            techo = medio - 1
         elif patente > patenteIngresada:
            piso = medio + 1
         medio = int((techo - piso))
         patente = self.__motos[medio].getPatente()
      if piso > techo:
         print(f"No se encontro el pedido con patente: {patenteIngresada}")
      else:
         print(f"La moto es de: {self.__motos[piso].getNyA()}, marca {self.__motos[piso].getMarca()} y tiene {self.__motos[piso].getKm()} Km")
  
  
   def ordenarMotos(self):
      self.__motos.sort()
  
  
   def listarComisiones(self, pedidos):
      self.ordenarMotos()
      for moto in self.__motos:
         patente = moto.getPatente()
         print(f"\n\nPatente de la moto: {patente}")
         print(f"Conductor: {moto.getNyA()}")
         pedidos.calcularComision(patente)