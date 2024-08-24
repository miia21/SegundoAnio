from gestorpublicacion import *
def test():
    lista=gestor()
    lista.carga()
    metallica=False
    while metallica==False:
        op=int(input("""Ingrese:
                     1: Crear nueva publicacion
                     2: Mostrar tipo
                     3: Mostrar cantidad de cada tipo
                     4: Mostrar todo
                     0: Cerrar ejecucion
                     : """))
        if op==1:
            lista.nuevo()
        elif op==2:
            lista.mostrartipo()
        elif op==3:
            lista.contartipo()
        elif op==4:
            lista.mostrartodo()
        elif op==0:
            print("BYE BYE")
            metallica=True

if __name__=='__main__':
    test()