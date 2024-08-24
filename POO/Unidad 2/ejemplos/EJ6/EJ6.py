from GestorCuentas import GestorC
from GestorTransacciones import controlaT
def menu():
    GC=GestorC()
    GT=controlaT()
    k=-1
    GC.test()
    GT.test()
    opcion=int(input("Ingrese la opcion a realizar: \n 1.Mostrar datos cliente \n 2.modificar porcentaje anual \n 3. guardar datos \n 4. Salir\n"))
    while k!=0:
        if(opcion==4):
            k=0
        elif(opcion==1):
            GC.mostrardat()
        elif(opcion==2):
            GC.modifA()
        elif(opcion==3):
            GC.guardarcuentas()
        opcion=int(input("Ingrese la opcion a realizar: \n 1.Mostrar datos cliente \n 2.modificar porcentaje anual \n 3. guardar datos \n 4. Salir\n"))
      
if __name__=='__main__':
    menu()