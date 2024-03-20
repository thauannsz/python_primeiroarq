from calculadora import soma

def teste_soma():
    assert soma(1, 2) == 3
    
def teste_soma_neg():
    assert soma(-1, -2) == -3
    
def teste_som_errada():
    assert soma(3, 4) == 10