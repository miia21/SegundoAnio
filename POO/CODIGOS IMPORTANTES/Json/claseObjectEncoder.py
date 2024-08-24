import json
from pathlib import Path
from claseGestorJugador import gestorJugador        #Importar todas las clases
from claseJugador import jugador

class objectEncoder(object):
    def decodificarDiccionario(self, d):
        if '__class__' not in d:
            return d
        else:
            class_name=d['__class__']
            class_=eval(class_name)
            if class_name=='gestorJugador':       #Modificar
                jugadores=d['jugadores']       #Modificar
                manejador=class_()
            for i in range(len(jugadores)):     #Modificar
                djugador=jugadores[i]     #Modificar
                class_name=djugador.pop('__class__')     #Modificar
                class_=eval(class_name)
                atributos=djugador['__atributos__']     #Modificar
                unJugador=class_(**atributos)     #Modificar
                manejador.agregarJugador(unJugador)     #Modificar
        return manejador
    
    def guardarJSONArchivo(self, diccionario, archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()

    def leerJSONArchivo(self, archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario=json.load(fuente)
            fuente.close()
            return diccionario