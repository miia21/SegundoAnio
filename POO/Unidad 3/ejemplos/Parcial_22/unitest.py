import unittest
from clase_servicio import Servicio
from clase_lista import Lista

class Test(unittest.TestCase):
    __lista : Lista
    def setUp(self):
        self.__lista = Lista()
    def test_agregar(self):
        servicio=Servicio("FNCS","Mondre","Meglioli","2024","100")
        self.__lista.agregar_al_final(servicio)
        self.assertIn( servicio , self.__lista , "El Servicio No se agrego correctamente a la lista")
if __name__=='__main__':
    unittest.main()