from lista import lista
def menu():
    k=-1
    P=lista()
    P.carga()
    while(k!=0):
        op=int(input(">>>>>>>>>>>>>>>>>>>>\ningresar una opcion:\n1.agregar una publicacion\n2.mostrar tipo de publicacion en un lugar de la lista\n3.mostrar cantidad de publicaciones de cada tipo\n4.Mostrar datos de todas las publicaciones\n5.Salir\n"))
        print("<<<<<<<<<<<<<<<<<<<<")
        if op==5:
            k=0
        if op==1:
            P.agregar()
        if op==2:
            P.mostrarclase()
        if op==3:
            P.muestracant()
        if op==4:
            P.muestradatos()
if __name__=='__main__':
    menu()