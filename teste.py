import unittest
from calculadora import soma

class Teste_Calculadora(unittest.TestCase):
    def teste_soma(self):
        self.assertEqual(soma(1,1), 2)
        self.assertEqual(soma(-1,3), 2)
        self.assertEqual(soma(-1,-1), -2)
    def teste_subt(self):
        self.assertEqual(subtracao(5,3), 9)
        
if __name__=='__main__':
    unittest.main()