from GestorEdificio import GestorE
def Menu ():
    #NOTA : El try vendria siendo el lugar donde va a estar la parte del codigo que se quiere controlar
    try:
        op = int(input("""
Menu de Opciones
            [1] Mostrar Datos
            [2] item 1 (busca un nombre y muestra a los de adentro)
            [3] muesta la superficie de un edificio que ingresas
            [4] Dado el nombre de un propietario decir la superficie y el porcentaje de dicha superficie en el edificio
            [5] Dar el numero de un piso y mostrar quienes tiene 3 dormitorios y mas de 1 baño
               -> """))
    #NOTA : los except son en caso de que la condicion no se cumpla tal y como se espera(LOS QUE ESTAN ABAJO EN EL MAIN TIENEN QUE TENER UN 'assert ban is True' EN EL GESTOR, DEBIDO A QUE COMPRUEBAN LA CONDICION EN OTRO MODULO)
    except ValueError:
        print("ERROR : Ingrese un numero por favor")
    return op

if __name__ == "__main__":
    print ("EN ESTE EJERCICIO SE HACE EL CASO DE LA COMPOCISION, PARA HACERLO SE HACE QUE LA CLASE CONTINENTE TENGO UN METODO PARA INICIALIZAR LA CLASE CONTENIDA")
    #NOTA: los calculos,los mostrar y las demas operaciones se hacen en las claces ya sea continente o contenido
    Edi = GestorE()
    opci = Menu()
    Edi.CargaArchivo()
    while opci != 0:
        if opci == 1:
            Edi.Mostrar()
            opci = Menu()
        elif opci == 2:
            try:
                print("Edificio Norte")
                nom = input("Ingrese el nombre de un edificio : " )
                Edi.BuscarPropied(nom)
            except AssertionError:
                print("No existe ese Edificio, Por favor tratar de nuevo")    
            opci = Menu()
        elif opci == 3:
            nom = input("Increse el nombre del edificio : ")
            Edi.SupEdifi(nom)
            opci = Menu()
        elif opci == 4:
            nom = input("Ingresar el nombre del propietari : ")
            Edi.SuperPropie(nom)
            opci = Menu()
        elif opci == 5:
            num = int(input("Ingrese un numero de piso : "))
            Edi.MostraCanti(num)
            opci = Menu()
        else:
            print("La pifiaste")
    print("Chau")
    #Edi.SupEdifi(nom)
