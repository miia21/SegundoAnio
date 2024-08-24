from gestoralquiler import gestoralquiler
from gestorcanchas import gestorcanchas

if __name__=='__main__':
    ga=gestoralquiler()
    gc=gestorcanchas()
    ga.testalquiler()
    gc.testcanchas()
    opc=int(input(' MENU DE OPCIONES\n 1-Listar los alquileres registrados ordenado\n 2-Ingresar identificador y mostrar total de minutos alquilado\n 0-Salir\n Ingrese Opcion:'))
    while (opc!=0):
        if(opc==1):
            ga.ordenar()
            ga.listado(gc)
            opc=input('\nIngrese Opcion:')
        elif(opc==2):
            ga.cantidadmin()
            opc=input('\nIngrese Opcion:')