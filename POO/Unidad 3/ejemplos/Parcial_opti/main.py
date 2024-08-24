from clase_lista import Lista
def menu():
    op=int(input("""
                 Menu de Opciones
    [1] Agregar Servicio 
    [2] Mostrar Todos Los Servicios Ordenados
    [3] Mostrar Cantidad de Embalajes que Superan los 50
    [4] Dada una Fecha de Servicio Mostrar nombre de servicio que mas contrataciones tuvo
    [0] Salir                
    --->"""))
    return op

if __name__ == '__main__':
    L=Lista()
    opcion=menu()
    while opcion != 0:
        if opcion==1:
            L.inciso_1()
            input("Presione Enter Para Continuar")
        elif opcion==2:
            L.inciso_2()
            input("Presione Enter Para Continuar")
        elif opcion==3:
            L.inciso_3()
            input("Presione Enter Para Continuar")
        elif opcion==4:
            L.inciso_4()
            input("Presione Enter Para Continuar")
        else:
            input("Opcion Invalida")    
        opcion=menu()
    print("Tenga un Gran Dia")
    
"""
1
1
Coca Cola
Marianito
Calle 13
2024
1000
50
90
Facultad Sociales
6
0
1
2
Fanta
Lautarito
Calle 20
2024
500
30
90
6
0
1
1
Fanta
Mondresito
Calle 30
2024
300
40
70
Facultad Sociales
3
"""