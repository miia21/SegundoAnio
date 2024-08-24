from claseObjectEncoder import objectEncoder
from claseGestorObjeto import gestorObjeto


if __name__=='__main__':
    json=objectEncoder()
    puntos = gestorObjeto()

    #Guardar objetos en archivo
    d=puntos.toJSON()
    json.guardarJSONArchivo(d,'datosPuntos.json')

    #Leer datos de un archivo json
    diccionario=json.leerJSONArchivo('datosPuntos.json')
    puntos=json.decodificarDiccionario(diccionario)