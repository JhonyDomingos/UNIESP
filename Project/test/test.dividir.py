import unittest

from calculadora import dividir

class TesteSomar(unittest.TestCase):
    
    def test_dividir_15_com_5(self):
        
        self.assertEqual(dividir(15, 5), 3) 


if __name__ == '__main__':
    unittest.main()