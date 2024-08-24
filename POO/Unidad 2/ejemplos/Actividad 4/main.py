import csv
from moduloGestorMotos import gestorMotos
from moduloGestorPedidos import gestorPedidos
def main():
   opcion = 1
   while opcion != 0:
      print("""Menú de opciones:
            Opcion 1: Leer los datos de las motos desde el archivo
            Opcion 2: Leer los datos de los pedidos desde el archivo
            Opcion 3: Cargar un nuevo pedido
            Opcion 4: Modificar tiempo real de entrega de un pedido
            Opcion 5: Mostrar tiempo promedio real de entrega y datos de un conductor
            Opcion 6: Mostrar listado con el pago de comisiones para cada moto
            Opcion 0: Detener la ejecucion""")
      opcion = int(input("Ingrese la opcion: "))
      if opcion == 1:
         motos = gestorMotos()
      elif opcion == 2:
         pedidos = gestorPedidos()
      elif opcion == 3:
         patente = input("Ingrese la patente: ")
         comidas = input("Ingrese las comidas: ")
         tiempo = int(input("Ingrese el tiempo (en segundos): "))
         precio = float(input("Ingrese el precio: "))
         pedidos.cargarPedido(patente,comidas,tiempo,precio)
      elif opcion == 4:
         patente = input("Ingrese la patente: ")
         identificador = int(input("Ingrese el identificador del pedido: "))
         tiempo = int(input("Ingrese el tiempo real (en segundos): "))
         pedidos.modificarTiempoReal(patente, identificador, tiempo)
      elif opcion == 5:
         patente = input("Ingrese una patente: ")
         motos.mostrarDatos(patente)
         pedidos.tiempoPromedio(patente)
      elif opcion == 6:
         motos.listarComisiones(pedidos)
      elif((opcion < 0) or (opcion > 6)):
         print("Opcion invalida")
if __name__ == "__main__":
   main()
""""Lote de prueba
1
2
4
A123BCD
1
600
4
A123BCD
4
300
5
A123BCD
"""