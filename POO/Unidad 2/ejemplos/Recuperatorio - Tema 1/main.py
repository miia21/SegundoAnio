from gestorcabañas import gestorcabañas
from gestorreservas import gestorreservas

if __name__=='__main__':
    gc=gestorcabañas()
    gr=gestorreservas()
    gc.testcabañas()
    gr.testreservas()
    print('MENU DE OPCIONES')
    opc=input('[1]-Ingresar Cantidad de huespedes y mostrar cabañas disponibles\n [2]-Ingresar Fecha y listar sus reservas\n [0]-Salir\n Ingrese opcion:')
    while opc!='0':
        if (opc=='1'):
            gc.mostrardisponibilidad(gr)
            opc=input('Ingrese opcion:')
        elif(opc=='2'):
            gr.listadofechas(gc)
            opc=input('Ingrese opcion:')