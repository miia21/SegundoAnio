from claseLista import lista
from interface import IArreglo
from zope.interface import Interface
from moduloObjectEncoder import objectEncoder

def agregarElemento(interface : IArreglo):
   interface.agregarElemento()

def insertarElemento(interface: IArreglo):
   try:
      indice = int(input("Ingrese el indice donde desea insertar: "))
   except ValueError:
      print("El valor ingresado debe ser un numero")
   else:
      interface.insertarElemento(indice)

def main():
   opcion = 1
   gestor = None
   encoder = objectEncoder()
   while(opcion != 0):
      opcion = input("""
Ingrese una opcion:
                     1) Agregar un agente
                     2) Insertar un agente
                     3) Mostrar el tipo de un agente
                     4) Mostrar todos los docentes investigadores de una carrera
                     5) Contar cantidad de investigadores y docentes investigadores
                     6) Mostrar todos los agentes ordenados por apellido
                     7) Calcular monto total de aportes extra
                     8) Guardar archivo JSON
                     9) Cargar desde JSON
                     10) Mostrar todos los agentes
                     0) Detener ejecucion
                     Ingrese una opcion: """)
      try:
         opcion = int(opcion)
      except ValueError:
         print("La opcion ingresada debe ser un numero")
      else:
         if opcion == 9:
            diccionario = encoder.cargarJSON()
            gestor = encoder.decodificarDiccionario(diccionario)
         elif gestor == None:
            gestor = lista()
         print("Se inicio un gestor vacio")
         if opcion == 1:
            agregarElemento(gestor)
         elif opcion == 2:
            insertarElemento(gestor)
         elif opcion == 3:
            indice = input("Ingrese el indice: ")
            gestor.mostrarTipo(indice)
         elif opcion == 4:
            carrera = input("Ingrese el nombre de la carrera: ")
            gestor.docentesInvestigadores(carrera)
         elif opcion == 5:
            area = input("Ingrese el area de investigacion: ")
            gestor.investigadores(area)
         elif opcion == 6:
            gestor.ordenarApellido()
         elif opcion == 7:
            categoria = input("Ingrese la categoria de incentivos: ")
            gestor.sumarExtras(categoria)
         elif opcion == 8:
            diccionario = gestor.toJSON()
            encoder.guardarJSON(diccionario)
         elif opcion == 10:
            gestor.mostrarTodo()
         elif opcion == 0:
            print("Deteniendo ejecucion...")
            
if __name__ == "__main__":
   main()