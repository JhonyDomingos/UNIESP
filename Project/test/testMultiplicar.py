import unittest

from calculadora import multiplicar

class TesteMultiplicar(unittest.TestCase):
    
    def test__multiplicar_10_com_5(self):
        
        self.assertEqual(multiplicar(10, 5), 50) 


if __name__ == '__main__':
    unittest.main()