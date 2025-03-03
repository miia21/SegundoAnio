from claseNodo import nodo

class digrafoEncadenado:
    __numVertices: int
    __listaVertices: list[nodo]

    def __init__(self, vertices):
        self.__numVertices = vertices
        self.__listaVertices = [None] * vertices

    def agregarArista(self, origen, destino, peso=1):
        if origen >= self.__numVertices or destino >= self.__numVertices:
            raise ValueError("Los vértices deben estar dentro del rango de la lista de adyacencia")
        
        nuevoNodo = nodo((destino, peso))
        nuevoNodo.setSiguiente(self.__listaVertices[origen])
        self.__listaVertices[origen] = nuevoNodo

    def mostrar(self):
        for i in range(self.__numVertices):
            print(f"Adyacentes de {i}: ", end="")
            aux = self.__listaVertices[i]
            while aux is not None:
                print(f"{aux.getObjeto()} ", end="")
                aux = aux.getSiguiente()
            print()

    def nodosAdyacentes(self, nodo):
        if nodo >= self.__numVertices:
            raise ValueError("El nodo debe estar dentro del rango de la lista de adyacencia")
        
        print("Los nodos adyacentes de ", nodo, "son : ", end="")
        aux = self.__listaVertices[nodo]
        while aux is not None:
            print(f"{aux.getObjeto()} ", end="")
            aux = aux.getSiguiente()
        print()

    def gradoNodo(self, nodo):
        if nodo >= self.__numVertices:
            raise ValueError("El nodo debe estar dentro del rango de la lista de adyacencia")
        
        aux = self.__listaVertices[nodo]
        grado = 0
        while aux is not None:
            grado += 1
            aux = aux.getSiguiente()
        print("El grado del nodo", nodo, " es ", grado)

    def camino(self, inicio, fin):
        visitados = [False] * self.__numVertices
        pila = [(inicio, [inicio])]

        while pila:
            nodoActual, camino = pila.pop()
            if nodoActual == fin:
                return camino
            if not visitados[nodoActual]:
                visitados[nodoActual] = True
                aux = self.__listaVertices[nodoActual]
                while aux is not None:
                    if not visitados[aux.getObjeto()[0]]:
                        pila.append((aux.getObjeto()[0], camino + [aux.getObjeto()[0]]))
                    aux = aux.getSiguiente()
        return None

    def conexo(self):
        visitados = [False] * self.__numVertices
        pila = [0]

        while pila:
            vertice = pila.pop()
            if not visitados[vertice]:
                visitados[vertice] = True
                aux = self.__listaVertices[vertice]
                while aux is not None:
                    if not visitados[aux.getObjeto()[0]]:
                        pila.append(aux.getObjeto()[0])
                    aux = aux.getSiguiente()

        return all(visitados)

    def aciclico(self):
        visitados = [False] * self.__numVertices
        
        def dfs(nodo, padre):
            visitados[nodo] = True
            aux = self.__listaVertices[nodo]
            while aux is not None:
                if not visitados[aux.getObjeto()[0]]:
                    if dfs(aux.getObjeto()[0], nodo):
                        return True
                elif aux.getObjeto()[0] != padre:
                    return True
                aux = aux.getSiguiente()
            return False

        for i in range(self.__numVertices):
            if not visitados[i]:
                if dfs(i, -1):
                    return False
        return True
    
    def dijkstra(self, origen):
        distancias = [float('inf')] * self.__numVertices
        distancias[origen] = 0
        conocidos = [False] * self.__numVertices
        camino = [-1] * self.__numVertices

        for _ in range(self.__numVertices):
            min_distancia = float('inf')
            v = -1
            for i in range(self.__numVertices):
                if not conocidos[i] and distancias[i] < min_distancia:
                    min_distancia = distancias[i]
                    v = i

            if v == -1:
                break

            conocidos[v] = True

            aux = self.__listaVertices[v]
            while aux is not None:
                if not conocidos[aux.getObjeto()[0]]:
                    peso = aux.getObjeto()[1]
                    if distancias[v] + peso < distancias[aux.getObjeto()[0]]:
                        distancias[aux.getObjeto()[0]] = distancias[v] + peso
                        camino[aux.getObjeto()[0]] = v
                aux = aux.getSiguiente()
            
        return distancias, camino
    
    def recorridoAnchura(self, inicio):
        visitados = [False] * self.__numVertices
        cola = [inicio]
        visitados[inicio] = True
        while cola:
            vertice = cola.pop(0)
            print(vertice, end=" ")
            aux = self.__listaVertices[vertice]
            while aux is not None:
                if not visitados[aux.getObjeto()[0]]:
                    visitados[aux.getObjeto()[0]] = True
                    cola.append(aux.getObjeto()[0])
                aux = aux.getSiguiente()

    def recorridoProfundidad(self, inicio):
        visitados = [False] * self.__numVertices
        pila = [inicio]
        visitados[inicio] = True
        while pila:
            vertice = pila.pop()
            print(vertice, end=" ")
            aux = self.__listaVertices[vertice]
            while aux is not None:
                if not visitados[aux.getObjeto()[0]]:
                    visitados[aux.getObjeto()[0]] = True
                    pila.append(aux.getObjeto()[0])
                aux = aux.getSiguiente()
