import unittest

def limpador_de_cpf(cpf):
    '''limpa o cpf'''
    lista = ''
    for i in cpf:
        if i.isdigit():
            lista += i
    return lista

def testador_de_cpf(Cpf):
    '''testa meu cpf'''
    contador1 = 10
    contador2 = 11
    contador3 = 0
    contador4 = 0
    p1 = 0
    p2 = 0
    CPF = limpador_de_cpf(Cpf)
    if len(CPF) != 11:
        return False
    while contador1 > 1:
        p1 += int(CPF[contador3]) * contador1
        contador1 -= 1
        contador3 += 1
    if (p1 * 10)% 11 == int(CPF[9]):
        while contador2 > 1:
            p2 += int(CPF[contador4]) * contador2
            contador2 -= 1
            contador4 += 1
        if (p2 * 10) % 11 == int(CPF[10]):
            return True
        else:
            return False
    else:
        return False
          
              
class MyTest(unittest.TestCase):
    
    def test(self):
        self.assertEqual(limpador_de_cpf("116.793.229-31"),"11679322931")
        self.assertEqual(limpador_de_cpf("116794009-16"),"11679400916")
        self.assertEqual(limpador_de_cpf("a123b456c789d00"),"12345678900")
        
    def test_testador_de_cpf(self):
        self.assertEqual(testador_de_cpf("116.793.229-31"),True)
        self.assertEqual(testador_de_cpf("116.793.229-32"),False)
        self.assertEqual(testador_de_cpf("11679322931"),True)
        self.assertEqual(testador_de_cpf("116"),False)  



if __name__ == "__main__":
    unittest.main()