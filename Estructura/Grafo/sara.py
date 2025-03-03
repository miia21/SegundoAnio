import numpy as np

class Grafo:
    __numVertices: int
    __matrizAdjacencia: np.ndarray

    def __init__(self, vertices):
        self.__numVertices = vertices
        self.__matrizAdjacencia = np.zeros((vertices, vertices), dtype=int)

    def agregarArista(self, origen, destino, peso=1):
        if origen >= self.__numVertices or destino >= self.__numVertices:
            raise ValueError("Los vértices deben estar dentro del rango de la matriz")
        self.__matrizAdjacencia[origen][destino] = peso
        self.__matrizAdjacencia[destino][origen] = peso

    def mostrar(self):
        for fila in self.__matrizAdjacencia:
            print(fila)

    def nodosAdyacentes(self, nodo):
        if nodo >= self.__numVertices:
            raise ValueError("El nodo debe estar dentro del rango de la matriz")
        else:
            adyacentes = []
            rango = self.__numVertices
            for i in range(rango):
                if self.__matrizAdjacencia[nodo][i] != 0:
                    adyacentes.append(i)
            print("Los nodos adyacentes de ", nodo, "son : ", end="")
            for j in range(len(adyacentes)):
                print(f"{adyacentes[j]} - ", end="")
            print()

    def gradoNodo(self, nodo):
        if nodo >= self.__numVertices:
            raise ValueError("El nodo debe estar dentro del rango de la matriz")
        else:
            print("El grado del nodo", nodo, " es ", np.sum(self.__matrizAdjacencia[nodo]))

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
        numVertices = len(self.__matrizAdjacencia)
        visitados = [False] * numVertices
        pila = [0]

        while pila:
            vertice = pila.pop()
            if not visitados[vertice]:
                visitados[vertice] = True
                for i in range(numVertices):
                    if self.__matrizAdjacencia[vertice][i] != 0 and not visitados[i]:
                        pila.append(i)

        return all(visitados)

    def aciclico(self):
        visitados = [False] * self.__numVertices
        
        def dfs(nodo, padre):
            visitados[nodo] = True
            for vecino in range(self.__numVertices):
                if self.__matrizAdjacencia[nodo][vecino] != 0:  # Si hay una conexión
                    if not visitados[vecino]:  # Si el vecino no fue visitado
                        if dfs(vecino, nodo):  # Llamada recursiva
                            return True
                    elif vecino != padre:  # Si el vecino es visitado y no es el padre, hay ciclo
                        return True
            return False
        
        for i in range(self.__numVertices):
            if not visitados[i]:  # Iniciar DFS en componentes no visitadas
                if dfs(i, -1):  # Si se encuentra un ciclo, el grafo no es acíclico
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
                if self.__matrizAdjacencia[vertice][i] == 1 and not visitados[i]:
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
                if self.__matrizAdjacencia[vertice][i] == 1 and not visitados[i]:
                    visitados[i] = True
                    pila.append(i)

    def dijkstra(self, origen):
        distancias = [float('inf')] * self.__numVertices
        distancias[origen] = 0
        visitados = [False] * self.__numVertices
        camino = [-1] * self.__numVertices

        for _ in range(self.__numVertices):
            min_distancia = float('inf')
            v = -1
            for i in range(self.__numVertices):
                if not visitados[i] and distancias[i] < min_distancia:
                    min_distancia = distancias[i]
                    v = i

            if v == -1:
                break

            visitados[v] = True

            for w in range(self.__numVertices):
                if self.__matrizAdjacencia[v][w] != 0 and not visitados[w]:
                    peso = self.__matrizAdjacencia[v][w]
                    if distancias[v] + peso < distancias[w]:
                        distancias[w] = distancias[v] + peso
                        camino[w] = v

        return distancias, camino