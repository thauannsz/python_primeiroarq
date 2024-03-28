from calculadora import media

def test_media():
    assert media([1, 2, 3, 4]) == 2.5
    
def wrong_test():
    assert media([2, 4, 6, 8]) == 27