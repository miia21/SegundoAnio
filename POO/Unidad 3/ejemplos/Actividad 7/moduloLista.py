import sys
sys.dont_write_bytecode = True
from interface import IArreglo
from zope.interface import implementer
from moduloPersonal import personal
from moduloApoyo import personalApoyo
from moduloDocente import docente
from moduloInvestigador import investigador
from moduloDocenteInvestigador import docenteInvestigador
from moduloNodo import nodo

@implementer(IArreglo)
class lista():
   __comienzo : nodo
   __actual : nodo
   __indice : int
   __tope : int

   def __init__(self):
      self.__comienzo = None
      self.__actual = None
      self.__indice = 0
      self.__tope = 0
   
   
   def __iter__(self):
      return self
   
   def __next__(self):
      if self.__indice == self.__tope:
         self.__actual = self.__comienzo
         self.__indice = 0
         raise StopIteration
      else:
         self.__indice += 1
         dato = self.__actual.datos()
         self.__actual = self.__actual.sig()
         return dato
   
   
   def crearAgente(self):
      cuil = input("Ingrese el cuil del agente: ")
      apellido = input("Ingrese el apellido del agente: ")
      nombre = input("Ingrese el nombre del agente: ")
      sueldoBasico = input("Ingrese el sueldo basico del agente: ")
      antiguedad = input("Ingrese la antiguedad del agente: ")
      try:
         sueldoBasico = float(sueldoBasico)
         antiguedad = int(antiguedad)
      except ValueError:
         print("El sueldo o la antiguedad no son correctas")
      else:
         tipo = input("""Ingrese el tipo de agente
                     1. Personal
                     2. Docente
                     3. Personal de apoyo
                     4. Investigador
                     5. Docente investigador
                     Opcion: """)
         try:
            tipo = int(tipo)
         except ValueError:
            print("El tipo ingresado debe ser un numero")
         else:
            if tipo == 1:
               agente = personal(cuil, apellido, nombre, sueldoBasico, antiguedad)
            if tipo == 2:
               carrera = input("Ingrese la carrera donde dicta clases: ")
               catedra = input("Ingrese la catedra donde dicta clases: ")
               cargo = input("Ingrese el cargo del docente: ")
               agente = docente(cuil, apellido, nombre, sueldoBasico, antiguedad, carrera, cargo, catedra)
            if tipo == 3:
               categoria = input("Ingrese la categoria: ")
               try:
                  categoria = int(categoria)
                  assert((categoria >= 0) and (categoria <= 22))
               except ValueError:
                  print("La categoria deve ser un numero")
               except AssertionError:
                  print("La categoria debe estar entre 1 y 22")
               else:
                  agente = personalApoyo(cuil, apellido, nombre, sueldoBasico, antiguedad, categoria)
            if tipo == 4:
               areaInvestigacion = input("Ingrese el area de investigacion: ")
               tipoInvestigacion = input("Ingrese el tipo de investigacion: ")
               agente = investigador(cuil, apellido, nombre, sueldoBasico, antiguedad, areaInvestigacion, tipoInvestigacion)
            if tipo == 5:
               carrera = input("Ingrese la carrera donde dicta clases: ")
               catedra = input("Ingrese la catedra donde dicta clases: ")
               cargo = input("Ingrese el cargo del docente: ")
               areaInvestigacion = input("Ingrese el area de investigacion: ")
               tipoInvestigacion = input("Ingrese el tipo de investigacion: ")
               aporteExtra = input("Ingrese el aporte extra por ser docente investigador: ")
               categoriaIncentivo = input("Ingrese la categoria de incentivo: ")
               try:
                  aporteExtra = float(aporteExtra)
                  categoriaIncentivo = int(categoriaIncentivo)
               except ValueError:
                  print("La categoria de incentivo y el aporte deben ser numeros")
               else:
                  agente = docenteInvestigador(cuil, apellido, nombre, sueldoBasico, antiguedad, areaInvestigacion, tipoInvestigacion, aporteExtra, categoriaIncentivo, carrera, cargo, catedra)
            return agente
               
            
            
   def insertarElemento(self, indice):
      agente = self.crearAgente()
      i = 0
      anterior = None
      actual = self.__comienzo
      while((actual != None) and (i != indice)):
         anterior = actual
         actual = actual.sig()
         i += 1
      if anterior == None:
         self.agregarElemento(agente)
      else:
         nuevoNodo = nodo(actual, agente)
         anterior.setSig(nuevoNodo)
         self.__tope += 1
   

   def agregarElemento(self, agente = None):
      if agente == None:
         agente = self.crearAgente()
      nuevoNodo = nodo(self.__comienzo, agente)
      self.__comienzo = nuevoNodo
      self.__actual = nuevoNodo
      self.__tope += 1
   
   
   def mostrarTodo(self):
      print("")
      for agente in self:
         print(f"{agente} con un sueldo de {agente.getSueldo():0.2f}")
      print("")
   
   
   def getTipo(self, dato):
      if isinstance(dato, docenteInvestigador):
         resultado = "Es de tipo Docente Investigador"
      elif isinstance(dato, docente):
         resultado = "Es de tipo Docente"
      elif isinstance(dato, investigador):
        resultado = "Es de tipo Investigador"
      elif isinstance(dato, personalApoyo):
         resultado = "Es de tipo Personal de Apoyo"
      elif isinstance(dato, personal):
         resultado = "Es de tipo Personal"
      return resultado
   
   
   def mostrarTipo(self, indice):
      try:
         indice = int(indice)
      except ValueError:
         print("El indice debe ser un numero")
      else:
         i = 0
         actual = self.__comienzo
         while((actual != None) and (i != indice)):
            actual = actual.sig()
            i += 1
         if i < self.__tope:
            if i == indice:
               dato = actual.datos()
               print(self.getTipo(dato))
         else:
            print("El indice ingresado esta fuera de rango")
            
   
   def docentesInvestigadores(self, carrera):
      arreAux = []
      for agente in self:
         if isinstance(agente, docenteInvestigador):
            if agente.getCarrera() == carrera:
               arreAux.append(agente)
      arreAux.sort()
      for docente in arreAux:
         print(docente)
         
   
   def investigadores(self, area):
      investigadores = 0
      docentes = 0
      for agente in self:
         if isinstance(agente, investigador):
            if agente.getAreaInvestigacion() == area:
               if isinstance(agente, docenteInvestigador):
                  docentes += 1
               else:
                  investigadores += 1
      print(f"Hay {docentes} docentes investigadores y {investigadores} investigadores")
   
   
   def ordenarApellido(self):
      arreAux = []
      for agente in self:
         arreAux.append(agente)
      arreAux.sort(key = lambda x : x.getApellido())
      for docente in arreAux:
         print(f"El agente: {docente} tiene un sueldo de: ${docente.getSueldo():0.2f}. {self.getTipo(docente)}")
   
   
   def sumarExtras(self, categoria):
      try:
         categoria = int(categoria)
      except ValueError:
         print("La categoria debe ser un numero")
      else:
         sumador = 0
         for agente in self:
            if isinstance(agente, docenteInvestigador):
               if agente.getCategoriaIncentivo() == categoria:
                  print(f"{agente.getApellido()} {agente.getNombre()} tiene un importe extra de: ${agente.getAporteExtra()}")
                  sumador += agente.getAporteExtra()
         print(f"El total de aportes extra es de: ${sumador:0.2f}")
   
   
   def agentesToJSON(self):
      arreglo = []
      for agente in self:
         arreglo.append(agente.toJSON())
      return arreglo
   
   
   def toJSON(self):
      diccionario = dict(
         clase = __class__.__name__,
         agentes = self.agentesToJSON()
      )
      return diccionario