import unittest


# n1 = int(input("Digite um número"))
# n2 = int(input("Digite um número"))


# resultado = n1 + n2

# print(resultado)

# def palavra reservada para função, dentro dos parenteses sao os parametros

def somar(num1, num2):
    return num1 + num2


# resultado = somar(10, 222)
# print(resultado)

# precisa criar uma class e dar um nome a ela e chamar o unittest.testcase
class TestSomar(unittest.TestCase):

    # toda função dentro da classe tem que ter o inicio test e precia do parametro self
    def test_somar_3_com_5(self):
        
        self.assertEqual(somar(3, 5), 8)
        print('TEST 1 Passed')
        

    def test_somar_8_com_75(self):

        self.assertEqual(somar(8, 75), 83)
        print('TEST 2 Passed ')
        
        
    def test_somar_1_com_1(self):
            
        self.assertEqual(somar(-1, -1), -2)
        print('TEST 3 passed')


if __name__ == '__main__':
    unittest.main()
