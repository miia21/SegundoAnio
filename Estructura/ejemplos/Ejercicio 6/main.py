from ColaEnlazada import Cola
import random

class Trabajo:
    __timepoimpression : int
    __timepollegada : int
    def __init__(self, tiempoimpresion, tiempollegada):
        self.__timepoimpression = tiempoimpresion
        self.__timepollegada = tiempollegada
    def __str__(self):
        return f"Tiempo de impresión: {self.__timepoimpression} Tiempo de llegada: {self.__timepollegada}"
    def getTiempoImpresion(self):
        return self.__timepoimpression
    def getTiempoLlegada(self):
        return self.__timepollegada
    def setTiempoImpresion(self, tiempoimpresion):
        self.__timepoimpression = tiempoimpresion


if __name__ == '__main__':
    cola = Cola()
    frecuencia = 5
    tms = 60
    reloj = 0
    tiempomax= 5
    ocupado = 0
    tiempoEsperaTotal = 0
    trabajosCompletados = 0
    trabajosNoCompletados = 0

    while reloj <= tms:
        if reloj % frecuencia == 0:
            tiempo = random.randint(1, 10)
            trabajo = Trabajo(tiempo,reloj)
            cola.insertar(trabajo)
            print(f"{trabajo}")
        if ocupado == 0 and not cola.vacio():
            trabajoActual = cola.suprimir()
            tiempoProceso = min(trabajoActual.getTiempoImpresion(), tiempomax)
            tiempoEspera = reloj - trabajoActual.getTiempoLlegada()
            trabajoActual.setTiempoImpresion(trabajoActual.getTiempoImpresion() - tiempoProceso)
            if trabajoActual.getTiempoImpresion() > 0:
                cola.insertar(trabajoActual)
            else:
                tiempoEsperaTotal += tiempoEspera
                trabajosCompletados += 1
                print(f"Se ha completado el trabajo {trabajoActual}\nTrabajos completados: {trabajosCompletados}\nTiempo total esperado: {tiempoEsperaTotal}\n")
            ocupado =  tiempoProceso
        else:
            reloj +=1
        if ocupado > 0:
            ocupado -= 1
    while not cola.vacio():
        trabajosNoCompletados += 1
        cola.suprimir()
    promedio = tiempoEsperaTotal / trabajosCompletados
    print(f"Promedio de tiempo de espera: {promedio}")
    print(f"Trabajos completados: {trabajosCompletados}")
    print(f"Trabajos no completados: {trabajosNoCompletados}")