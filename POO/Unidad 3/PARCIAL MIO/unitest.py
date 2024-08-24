import unittest
from claseLista import lista
from claseServicio import servicio

class test(unittest.TestCase):
    __lista: lista
    def setUp(self):
        self.__lista = lista()
    def testLista(self):
        ser=servicio("Mayo", "Mia", "Pocito", "30/05/24", 5000)
        self.__lista.agregarFinal(ser)
        self.assertIn(ser, self.__lista, "error, no se agrego el elemento")

if __name__=='__main__':
    unittest.main()
    

