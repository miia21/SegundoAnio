from ClasePila import pilaEnlazada
def main():
   torre1 = pilaEnlazada()
   torre2 = pilaEnlazada()
   torre3 = pilaEnlazada()
   torre1.insertar(4)
   torre1.insertar(3)
   torre1.insertar(2)
   torre1.insertar(1)
   torres = [torre1, torre2, torre3]
   print("El estado de las torres es:")
   for i in range(3):
      print(f"Torre {i+1}", end=": ")
      for dato in torres[i]:
         print(dato, end=" ")
      print()
   while not torre3.llena():
      sacar = int(input("Escriba la torre de la que desea sacar un disco: "))
      disco = torres[sacar-1].suprimir()
      if disco != None:
         poner = int(input("Escriba la torre de la que desea poner un disco: "))
         aux = torres[poner-1].suprimir()
         if aux == None:
            torres[poner-1].insertar(disco)
         elif aux > disco:
            torres[poner-1].insertar(aux)
            torres[poner-1].insertar(disco)
         else:
            print("El disco no puede ser colocado en la torre porque es mayor que el que hay en ella")
            torres[sacar-1].insertar(disco)
            torres[poner-1].insertar(aux)
      else:
         print("No hay discos en la torre")
      print("El estado de las torres es:")
      for i in range(3):
         print(f"Torre {i+1}", end=": ")
         for dato in torres[i]:
            print(dato, end=" ")
         print()
   print("GANASTE!!!")

if __name__ == "__main__":
   main()