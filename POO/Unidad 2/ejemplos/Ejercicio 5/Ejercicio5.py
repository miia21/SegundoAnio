from gestorEquipo import GestorEquipo
from gestorFechas import GestorFechas

def Menu():
    print("=================================MENU DE OPCIONES==========================================")
    print("a) Leer los datos de los equipos del archivo y almacenarlos en el Gestor de Equipos.")
    print("b) Leer los datos de las Fechas de Fútbol, y almacenarlos en el Gestor de Fechas.")
    print("c) Leer el nombre de un equipo y obtener un listado")
    print("d) Actualizar la tabla de todos los equipos, con los resultados de las fechas disputadas.")
    print("e) Ordenar la tabla de posiciones de mayor a menor")
    print("f) Almacenar la tabla de posiciones ordenada")
    print("g) SALIR")
    print("===========================================================================================")


if __name__ == '__main__':
    ge = GestorEquipo()
    gf = GestorFechas()
    while True:
        Menu()
        o = input("\nIngresar una opcion: ")
        if (o=='a'):
            ge.cargaEquipo()
            print("Se cargaron los equipos con exito\n")
        elif (o == 'b'):
            gf.cargaFechas()
            print("Se cargaron las fechas con exito\n")
        elif (o == 'c'):
            ge.buscar(gf)
        elif (o == 'd'):
            ge.actualizar(gf)
            print("Los equipos se actualizaron con exito\n")
        elif (o == 'e'):
            ge.ordenar()
        elif (o == 'f'):
            ge.almacenar()
        elif (o == 'g'):
            print("ADIOS\n")
            break
        else:
            print("Opcion no valida, intentar denuevo\n")