import json
from pathlib import Path
from claseLista import lista
from pathlib import Path
from clasePersonal import Personal
from claseApoyo import personalApoyo
from claseDocente import docente
from claseInvestigador import investigador
from claseDocenteInvestigador import docenteInvestigador
class objectEncoder:
   def guardarJSON(self, diccionario):
      with (Path(__file__).parent / "personal.json").open("w", encoding="UTF-8") as destino:
         json.dump(diccionario, destino, indent=4)
         destino.close()
      print("Se guardo el archivo")
      
      
   def cargarJSON(self):
      with (Path(__file__).parent / "personal.json").open("r", encoding="UTF-8") as fuente:
         diccionario = json.load(fuente)
         fuente.close
      print("Se leyo el archivo")
      return diccionario
   
   
   def decodificarDiccionario(self, d):
      if "clase" not in d:
         return d
      else:
         class_name = d["clase"]
         class_ = eval(class_name)
         if class_name == "lista":
            agentes = d["agentes"]
            gestor = lista()
            for i in range(len(agentes)):
               dAgente = agentes[i]
               class_name = dAgente.pop("clase")
               class_=eval(class_name)
               atributos = dAgente["atributos"]
               unAgente = class_(**atributos)
               gestor.agregarElemento(unAgente)
         return gestor