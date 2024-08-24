from gestorVehiculo import gestorVehiculo


def main():
   opcion = 1
   gv = gestorVehiculo()
   gv.cargaVehiculo()
   while(opcion != 0):
        opcion = input("""
                    Ingrese una opcion:
                     1) Agregar nuevo vehiculo
                     2) Mostrar el tipo de un vehiculo
                     3) Contar la cantidad de vehiculos de cada tipo
                     4) Mostrar todos los vehiculos
                     0) Detener ejecucion
                     Ingrese una opcion: \n""")
        try:
            opcion = int(opcion)
        except ValueError:
            print("La opcion ingresada debe ser un numero")
        else:
            if opcion == 1:
                gv.agregarVehiculo()
            elif opcion == 2:
                gv.mostrarTipo()
            elif opcion == 3:
                gv.contarCant()
            elif opcion == 4:
                gv.mostrar()
            elif opcion == 0:
                print("Deteniendo ejecucion...")
            
if __name__ == "__main__":
   main()