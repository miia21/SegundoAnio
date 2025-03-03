import numpy as np

class digrafoSecuencial:
    def __init__(self, vertices):
        self.__numVertices = vertices
        self.__matrizAdjacencia = np.zeros((vertices, vertices), dtype=int)

    def agregarArista(self, origen, destino, peso=1):
        if origen >= self.__numVertices or destino >= self.__numVertices:
            raise ValueError("Los vértices deben estar dentro del rango de la matriz")
        self.__matrizAdjacencia[origen][destino] = peso

    def mostrar(self):
        print("Matriz de Adyacencia:")
        for fila in self.__matrizAdjacencia:
            print(fila)

    def nodosAdyacentes(self, nodo):
        if nodo >= self.__numVertices:
            raise ValueError("El nodo debe estar dentro del rango de la matriz")
        
        print(f"Nodos adyacentes a {nodo}: ", end="")
        for i in range(self.__numVertices):
            if self.__matrizAdjacencia[nodo][i] != 0:
                print(f"{i} (peso {self.__matrizAdjacencia[nodo][i]})", end=", ")
        print()

    def gradoNodo(self, nodo):
        if nodo >= self.__numVertices:
            raise ValueError("El nodo debe estar dentro del rango de la matriz")
        
        grado = np.sum(self.__matrizAdjacencia[nodo] != 0)
        print(f"El grado del nodo {nodo} es {grado}")

    def camino(self, inicio, fin):
        visitados = [False] * self.__numVertices
        pila = [(inicio, [inicio])]

        while pila:
            nodoActual, camino = pila.pop()
            if nodoActual == fin:
                return camino
            if not visitados[nodoActual]:
                visitados[nodoActual] = True
                for vecino in range(self.__numVertices):
                    if self.__matrizAdjacencia[nodoActual][vecino] != 0 and not visitados[vecino]:
                        pila.append((vecino, camino + [vecino]))
        return None

    def conexo(self):
        visitados = [False] * self.__numVertices
        pila = [0]

        while pila:
            vertice = pila.pop()
            if not visitados[vertice]:
                visitados[vertice] = True
                for i in range(self.__numVertices):
                    if self.__matrizAdjacencia[vertice][i] != 0 and not visitados[i]:
                        pila.append(i)

        return all(visitados)

    def aciclico(self):
        visitados = [False] * self.__numVertices

        def dfs(nodo, padre):
            visitados[nodo] = True
            for vecino in range(self.__numVertices):
                if self.__matrizAdjacencia[nodo][vecino] != 0:
                    if not visitados[vecino]:
                        if dfs(vecino, nodo):
                            return True
                    elif vecino != padre:
                        return True
            return False

        for i in range(self.__numVertices):
            if not visitados[i]:
                if dfs(i, -1):
                    return False
        return True

    def recorridoAnchura(self, inicio):
        visitados = [False] * self.__numVertices
        cola = [inicio]
        visitados[inicio] = True
        while cola:
            vertice = cola.pop(0)
            print(vertice, end=" ")
            for i in range(self.__numVertices):
                if self.__matrizAdjacencia[vertice][i] != 0 and not visitados[i]:
                    visitados[i] = True
                    cola.append(i)

    def recorridoProfundidad(self, inicio):
        visitados = [False] * self.__numVertices
        pila = [inicio]
        visitados[inicio] = True
        while pila:
            vertice = pila.pop()
            print(vertice, end=" ")
            for i in range(self.__numVertices):
                if self.__matrizAdjacencia[vertice][i] != 0 and not visitados[i]:
                    visitados[i] = True
                    pila.append(i)
