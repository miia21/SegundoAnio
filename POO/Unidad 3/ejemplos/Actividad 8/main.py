import sys
sys.dont_write_bytecode = True
from moduloLista import lista
from interface import IArreglo
from zope.interface import Interface
from moduloObjectEncoder import objectEncoder
from moduloInterfaceDirector import IDirector
from moduloInterfaceTesorero import ITesorero

def agregarElemento(interface : IArreglo):
   interface.agregarElemento()

def insertarElemento(interface: IArreglo):
   try:
      indice = int(input("Ingrese el indice donde desea insertar: "))
   except ValueError:
      print("El valor ingresado debe ser un numero")
   else:
      interface.insertarElemento(indice)

def director(dire : IDirector):
   usuario = input("Ingrese el usuario: ")
   contrasena = input("Ingrese la contraseña: ")
   opcion = 1
   if((usuario == "uDirector") and (contrasena == "ufC77#!1")):
      while opcion != 0:
         opcion = input("""Ingrese una opcion:
                        1) Modificar el sueldo basico de un agente
                        2) Modificar el porcentaje por categoria de un personal de apoyo
                        3) Modificar importe extra a un docente investigador
                        4) Modificar porcentaje por cargo de docente
                        0) Cerrar sesion
                        Ingrese una opcion: """)
         try:
            opcion = int(opcion)
         except ValueError:
            print("La opcion debe ser un numero")
         else:
            if opcion == 0:
               print("Cerrando sesion...")
            else:
               dni = input("Ingrese el dni del agente a modificar: ")
               if opcion == 1:
                  try:
                     nuevoSueldo = float(input("Ingrese el nuevo sueldo basico: "))
                  except ValueError:
                     print("El sueldo debe ser un numero")
                  else: 
                     dire.modificarBasico(dni, nuevoSueldo)
               elif opcion == 2:
                  try:
                     nuevoPorcentaje = float(input("Ingrese el nuevo porcentaje: "))
                  except ValueError:
                     print("El porcentaje debe ser un numero")
                  else: 
                     dire.modificarPorcentajePorCategoria(dni, (nuevoPorcentaje/100))
               elif opcion == 3:
                  try:
                     nuevoImporte = float(input("Ingrese el nuevo importe extra: "))
                  except ValueError:
                     print("El importe debe ser un numero")
                  else: 
                     dire.modificarImporteExtra(dni, nuevoImporte)
               elif opcion == 4:
                  try:
                     nuevoPorcentaje = float(input("Ingrese el nuevo porcentaje por cargo: "))
                  except ValueError:
                     print("El porcentaje debe ser un numero")
                  else: 
                     dire.modificarPorcentajePorCargo(dni, (nuevoPorcentaje/100))
   else:
      print("Datos de acceso incorrectos")
def tesorero(teso : ITesorero):
   usuario = input("Ingrese el usuario: ")
   contrasena = input("Ingrese la contraseña: ")
   if((usuario == "uTesoreso") and (contrasena == "g@74ck")):
      dni = input("Ingrese el dni del agente a mostrar sueldo: ")
      teso.gastosSueldoPorEmpleado(dni)
   else:
      print("Datos de acceso incorrectos")
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
                     11) Acceder como tesorero
                     12) Acceder como director
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
         elif opcion == 11:
            tesorero(gestor)
         elif opcion == 12:
            director(gestor)
         elif opcion == 0:
            print("Deteniendo ejecucion...")
            
if __name__ == "__main__":
   main()
   
   
"""Lote de prueba
1
20-44991289-7
Sasso
Joaquin
457895.84
15
5
Geologia
Piedras
exclusivo
Atmosfera
Cientifica
34552.44
2
1
20-45885130-4
Reynoso
Nicolas
20.50
1
3
13
1
20-45263619-1
Reta
German
1024719.43
20
5
Geologia
Paleontologia
exclusivo
Atmosfera
Laboratorio
352789.69
1
2
2
20-46886131-5
Valiente
Lucas
124532.01
2
1
2
0
20-43342543-3
Spesia
Tomas
765342.99
15
2
LCC
Algoritmos y Resolucion de Problemas
semiexclusivo
1
20-272872619-3
Perez
Gabriel
1324719.43
30
4
Atmosfera
Laboratorio
1
27-457632687-5
Pastor
Mia
324719.43
4
5
LSI
Bases de datos
simple
SQLAlchemy
Computacion
35789.69
2
1
20-453632387-5
Rodriguez
Pedro
374719.43
4
5
LSI
Bases de datos
simple
SQLAlchemy
Computacion
25981.69
3
1
20-453633787-2
Sanchez
Pedro
304719.43
4
5
LSI
Bases de datos
semiexclusivo
SQLAlchemy
Computacion
12981.69
3
1
20-323632387-9
Martinez
Pedro
584719.43
4
5
LSI
Bases de datos
semiexclusivo
SQLAlchemy
Computacion
96981.69
4
1
20-253632387-3
Fernandez
Pedro
534722.43
4
5
LSI
Bases de datos
simple
SQLAlchemy
Computacion
16721.69
5
"""
