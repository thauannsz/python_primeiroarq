import unittest
from calculadora import soma, subtracao, divisao

class Teste_Calculadora(unittest.TestCase):
    def teste_soma(self):
        self.assertEqual(soma(1,1), 2)
        self.assertEqual(soma(-1,3), 3)
        
    def teste_subt(self):
        self.assertEqual(subtracao(5,3), 2)
        self.assertEqual(subtracao(5,3), 9)
        
    def teste_div(self):
        self.assertEqual(divisao(8,4), 2)
        self.assertEqual(divisao(4,2), 3)
        
if __name__=='__main__':
    unittest.main()
    
    
    
    
    
    
    
    
