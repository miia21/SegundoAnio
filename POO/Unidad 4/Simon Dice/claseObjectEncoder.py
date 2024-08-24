import json
from pathlib import Path
from claseGestorJugador import gestorJugador
from claseJugador import jugador

class objectEncoder(object):
    def decodificarDiccionario(self, d):
        if '__class__' not in d:
            return d
        else:
            class_name=d['__class__']
            class_=eval(class_name)
            if class_name=='gestorJugador':
                jugadores=d['jugadores']
                manejador=class_()
            for i in range(len(jugadores)):
                djugador=jugadores[i]
                class_name=djugador.pop('__class__')
                class_=eval(class_name)
                atributos=djugador['__atributos__']
                unJugador=class_(**atributos)
                manejador.agregarJugador(unJugador)
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