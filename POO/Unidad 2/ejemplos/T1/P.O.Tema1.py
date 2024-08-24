from manejadorDeFederados import *
from manejadorDePuntos import *
if __name__=='__main__':
    manejadorF=manejadorFederados()
    manejadorF.cargarManejador()
    manejadorF.mostrarManejadorF()
    manejadorP=manejadorPuntaje()
    manejadorP.cargarManejadorP()
    manejadorP.mostrarManejadorP()
    print("1.Punto a\n2.Punto b\n3.Punto c\n4.Punto d\n0.Salir\n")
    i=int(input("Ingrese una opción: "))
    while i!=0:
        if i==1:
            manejadorP.puntoA()
        print("\n1.Punto a\n2.Punto b\n3.Punto c\n4.Punto d\n0.Salir\n")
        i=int(input("Ingrese una opción: "))