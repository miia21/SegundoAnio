import numpy as np

class grafoSecuencial:
    __matriz: np.ndarray
    __nodos: int

    def __init__(self, nodos):
        self.__nodos = nodos
        self.__matriz = np.zeros((nodos, nodos), dtype=int)

    def agregarArista(self, origen, destino, peso):
        self.__matriz[origen][destino] = peso
        self.__matriz[destino][origen] = peso

    def eliminarArista(self, origen, destino):
        self.__matriz[origen][destino] = 0
        self.__matriz[destino][origen] = 0

    def imprimirGrafo(self):
        for i in range(self.__nodos):
            for j in range(self.__nodos):
                print(self.__matriz[i][j], end=" ")
            print()

    def adyacentes(self, nodo):
        adyacentes = []
        for i in range(self.__nodos):
            if self.__matriz[nodo][i] != 0:
                adyacentes.append(i)
        return adyacentes
    
    def dijkstra(self, origen):
        distancias = [float('inf')] * self.__nodos  # Usamos infinito como valor inicial
        distancias[origen] = 0  # Distancia al origen es 0
        conocidos = [False] * self.__nodos  # Conjunto de nodos conocidos
        camino = [-1] * self.__nodos  # Predecesores para reconstruir el camino

        for _ in range(self.__nodos):
            min_distancia = float('inf')
            v = -1
            for i in range(self.__nodos):
                if not conocidos[i] and distancias[i] < min_distancia:
                    min_distancia = distancias[i]
                    v = i

            if v == -1:  # Si no encontramos un nodo válido, terminamos
                break

            conocidos[v] = True  # Marcamos el nodo como conocido

            for w in self.adyacentes(v):
                if not conocidos[w]:  # Si w no es conocido
                    peso = self.__matriz[v][w]
                    if distancias[v] + peso < distancias[w]:
                        distancias[w] = distancias[v] + peso  # Actualizamos la distancia
                        camino[w] = v  # Actualizamos el predecesor

        return distancias, camino

    def camino(self, u, v):
        distancias, predecesores = self.dijkstra(u)

        if distancias[v] == float('inf'):
            return f"Error: El nodo {v} no es alcanzable desde el nodo {u}."

        camino = []
        actual = v
        while actual != -1:
            camino.insert(0, actual)
            actual = predecesores[actual]

        return camino