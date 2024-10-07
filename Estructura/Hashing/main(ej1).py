from hashDirAbierto import tablaHashing
import random

def menu():
    print("Menu\n 1-Mostrar\n 2-Buscar\n 3-Salir\n")

def main():
    hashTable = tablaHashing()
    hashTable.insert(40000000)
    for i in range(100):
        hashTable.insert(random.randint(40000000, 47000000))
    menu()
    opcion = int(input("Ingrese una opcion: \n"))
    while opcion != 3:
        if opcion == 1:
            hashTable.display()
        elif opcion == 2:
            key = int(input("Ingrese la clave a buscar: \n"))
            hashTable.search(key)
        else:
            print("Opcion invalida")
        menu()
        opcion = int(input("Ingrese una opcion: \n"))

if __name__ == "__main__":
    main()
    