from moduloPedido import pedido
import csv
class gestorPedidos:
   __pedidos = []
   __id : int
   def __init__(self):
      archivoPedidos = open("datosPedidos.csv")
      reader = csv.reader(archivoPedidos, delimiter=";")
      bandera = False
      self.__id = 0
      for fila in reader:
         if bandera == False:
            bandera = True
         else:
            self.__id += 1
            objeto = pedido(fila[0],fila[1],fila[2],fila[3],fila[4])
            self.__pedidos.append(objeto)
      archivoPedidos.close()
      
      
   def mostrarPedidos(self):
      for pedido in self.__pedidos:
         pedido.mostrarDatos()
         
         
   def cargarPedido(self, patente, comidas, tiempo, precio):
      objeto = pedido(patente, self.__id, comidas, tiempo, precio)
      self.__pedidos.append(objeto)
      
      
   def buscarPatente(self, patenteIngresada):
      self.__pedidos.sort()
      piso = 0
      techo = len(self.__pedidos) -1
      medio = int((techo + piso) / 2)
      while((piso < techo) and (patenteIngresada != self.__pedidos[medio].getPatente())):
         patente = self.__pedidos[medio].getPatente()
         if patente < patenteIngresada:
            piso = medio + 1
         if patente > patenteIngresada:
            techo = medio - 1
         medio = int((techo + piso) / 2)
      if piso >= techo:
         print(f"No se encontro el pedido con patente: {patenteIngresada}")
      return medio
   
   
   def primerCoincidencia(self, patente):#Coloca el indice del primer pedido que tenga patente
      i = self.buscarPatente(patente)
      if i > 0: 
         while (((i-1) >= 0 ) and (patente == self.__pedidos[i-1].getPatente())):
            i -= 1
      return i
   
   
   def modificarTiempoReal(self, patenteIngresada, id, tiempo):
      indice = self.primerCoincidencia(patenteIngresada)
      while (((indice+1) < len(self.__pedidos)) and (id != self.__pedidos[indice].getID())):
         indice += 1
      if (patenteIngresada == self.__pedidos[indice].getPatente()):
         self.__pedidos[indice].setTiempoReal(tiempo)
      else:
         print("No se encontro un pedido con ese identificador y patente")
         
         
   def tiempoPromedio(self, patenteIngresada):
      piso = self.buscarPatente(patenteIngresada)
      acumulador = 0
      contador = 0
      if piso > 0: #Coloca piso en el indice del primer pedido que tenga patenteIngresada
         while (((piso-1) >= 0 ) and (patenteIngresada == self.__pedidos[piso-1].getPatente())):
            piso -= 1
      while (((piso) < (len(self.__pedidos)-1)) and (patenteIngresada == self.__pedidos[piso].getPatente())):
         acumulador += self.__pedidos[piso].getTiempoReal()
         contador += 1
         piso += 1
      total = acumulador / contador
      minutos = int(total / 60)
      segundos = int(total % 60)
      print(f"El tiempo real promedio del repartidor es de: {minutos}:{segundos}")
      
      
   def calcularComision(self, patente):
      indice = self.primerCoincidencia(patente)
      total = 0.0
      print("Id de pedido   Tiempo Estimado   Tiempo Real    Precio")
      while ((indice < len(self.__pedidos)) and (patente == self.__pedidos[indice].getPatente())):
         identificador = self.__pedidos[indice].getID()
         tiempoE = self.__pedidos[indice].getTiempoEstimado()
         tiempoR = self.__pedidos[indice].getTiempoReal()
         precio = float(self.__pedidos[indice].getPrecio())
         print(f"{identificador}                 {tiempoE}                 {tiempoR}           {precio}")
         indice+= 1
         total += precio
      print(f"Total:                                              {total:0.2f}")
      comision = total * 0.2
      print(f"Comision: ${comision:0.2f} (20% del total)")
         