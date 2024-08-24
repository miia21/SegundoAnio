from gestor_canchas import gestor_can
from gestor_alquiler import gestor_al
def menu():
    op=int(input("""
                 Menu de Opciones
    [1] Listado de Alquileres
    [2] Tiempo de alquiler por cancha
    [0] Salir                
    --->"""))
    return op

if __name__ == '__main__':
    opcion=menu()
    GA=gestor_al()
    GC=gestor_can()
    while opcion != 0:
        if opcion==1:
            GA.listar_reservas(GC)
            input("Presione Enter Para Continuar")
        elif opcion==2:
            GA.alquiler_total()
            input("Presione Enter Para Continuar")
        else:
            input("Opcion Invalida")    
        opcion=menu()
    print("Tenga un Gran Dia") 