import numpy as np

class tablaHashing:
    __M: int
    __tabla: np.ndarray

    def __init__(self):
        self.__M = 1009
        self.__tabla = np.full(self.__M, None, dtype=object)
        
    def hashDiv(self, key):
        return key % self.__M

    def hashExt(self, key):
        strKey = str(key)
        numKey = int(strKey[-3:])
        return numKey % self.__M

    def hashPleg(self, key):
        strKey = str(key)
        sum=0
        for i in range(0, len(strKey), 2):
            sum += int(strKey[i:i+2])
        return sum % self.__M

    def hashCuadMedio(self, key):
        strKey = str(key**2)
        medio = len(strKey) // 2
        if medio % 2 == 0:
            return int(strKey[medio-1:medio+1]) % self.__M
        else:
            return int(strKey[medio]) % self.__M
        
    def hashClaveAlfa(self, key):
        strKey = str(key)
        suma = 0
        for i, char in enumerate(strKey):
            valor_ascii = ord(char)
            suma += valor_ascii * (i)
        return suma % self.__M

    def insert(self, key):
        index = self.hashDiv(key)
        if self.__tabla[index] == None:
            self.__tabla[index] = key
        else:
            i = 1
            while i < self.__M:
                newIndex = (index + i) % self.__M
                if self.__tabla[newIndex] == None:
                    self.__tabla[newIndex] = key
                    break
                i += 1
    
    def search(self, key):
        index = self.hashDiv(key)
        longi=1
        if self.__tabla[index] == key:
            print("Se encontro el valor, en la posicion: ", index+1)
            print("Longitud de la busqueda: ", longi)
        else:
            i = 1
            while i < self.__M:
                newIndex = (index + i) % self.__M
                longi+=1
                if self.__tabla[newIndex] == key:
                    print("Se encontro el valor, en la posicion: ", newIndex+1)
                    print("Longitud de la busqueda: ", longi)
                i += 1
            if i > self.__M:
                print("No se encontro el valor")
                print("Longitud de la busqueda: ", longi)
    
    def display(self):
        for i in range(self.__M):
            print(i+1, ":", self.__tabla[i])