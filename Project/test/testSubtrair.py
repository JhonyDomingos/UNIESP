import unittest

from calculadora import subtrair
class TesteSubtrair(unittest.TestCase):
    
    def test_subtrair_55_com_5(self):
        
        self.assertEqual(subtrair(25, 5), 20) 


if __name__ == '__main__':
    unittest.main()