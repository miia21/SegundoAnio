import numpy as np

class tablaHashing:
    __M: int
    __b: int
    __tabla: np.ndarray
    __overflow: np.ndarray
    __i: int

    def __init__(self):
        self.__M = 337
        self.__b= 5
        self.__tabla = np.full((self.__M, self.__b), None, dtype=object)
        self.__overflow = np.full(int(self.__M *self.__b *0.2), None, dtype=object)
        self.__i = 0

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
        if self.__ocupados[index] < self.__b:
            self.__tabla[index][self.__ocupados[index]] = key
            self.__ocupados[index] += 1
            return
        if self.__i < len(self.__overflow):
            self.__overflow[self.__i] = key
            self.__i += 1
        else:
            print("No hay espacio para insertar el valor")
    
    def search(self, key):
        index = self.hashDiv(key)
        longi = 1
        for i in range(self.__ocupados[index]):
            if self.__tabla[index][i] == key:
                print("Se encontró el valor en el bucket:", index + 1)
                print("Longitud de la búsqueda:", longi)
                return
            longi += 1
        for i in range(self.__i):
            if self.__overflow[i] == key:
                print("Se encontró el valor en el área de overflow")
                print("Longitud de la búsqueda:", longi)
                return
            longi += 1
        print("No se encontró el valor")
    
    def display(self):
        print("Área Primaria:")
        for i, bucket in enumerate(self.__tabla):
            print(f"Bucket {i + 1} ({self.__ocupados[i]} ocupados): {bucket}")
        print("\nÁrea de Overflow:")
        for i, entry in enumerate(self.__overflow):
            if entry is not None:
                print(f"Overflow {i + 1}: Clave {entry}")