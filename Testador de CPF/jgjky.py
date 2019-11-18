import unittest

def soma(valor_a,valor_b):
    return valor_a + valor_b

def impares(lista):
    lista2 = []
    for numero in lista:
        if numero %2 == 1:
            lista2.append(numero)
    return lista2

class MyTest(unittest.TestCase):

    def test(self):
        self.assertEqual(soma(4, 3), 7)

    def test_impares(self):
        self.assertEqual(impares([3, 8, 1, 5, 0, -3]),[3, 1, 5, -3])
        self.assertEqual(impares([2,6,-2,10,4]),[])
        self.assertEqual(impares([]),[])
        self.assertEqual(impares([1,3,9,5]),[1,3,9,5])

if __name__ == "__main__":
    unittest.main()