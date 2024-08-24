from claseLista import lista


if __name__ == '__main__':
    Viajeros = lista()
    Viajeros.cargaLista()
    a=Viajeros.buscarViajero()
    #Viajeros.mostraViajeros()
    print(f"MENU")
    print(f"a-Consultar de Millas")
    print(f"b- Acumular Millas")
    print(f"c- Canjear Millas")
    o = input('Elige una opcion:')
    if o == 'a':
        Viajeros.cantidadTotaldeMillas(a)
    elif o == 'b':
        Viajeros.acumularMillas(a)
    elif o == 'c':
        Viajeros.canejarMillas(a)
    else:
        print(f"OPCION NO ENCONTRADA")