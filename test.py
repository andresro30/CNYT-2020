import unittest
import calculadora


class TestCalculadora(unittest.TestCase):

    def test_suma(self):
        cor1 = [4,6]
        cor2 = [1,-5]
        ans = calculadora.suma(cor1,cor2)
        self.assertEqual(ans,[5,1])


    def test_resta(self):
        cor1 = [4,18]
        cor2 = [1,-5]
        ans = calculadora.resta(cor1,cor2)
        self.assertEqual(ans,[3,23])

    def test_multiplicacion(self):
        cor1 = [4,6]
        cor2 = [1,4]
        ans = calculadora.multiplicacion(cor1,cor2)
        self.assertEqual(ans,[-20,22])

    def test_division(self):
        cor1 = [3,2]
        cor2 = [1,-2]
        ans = calculadora.division(cor1,cor2)
        self.assertEqual(ans,[-0.2,1.6])

    def test_modulo(self):
        cor1 = [1,5]
        cor2 = [3,7]
        self.assertEqual(calculadora.modulo(cor1)[0],5.0990195135927845)
        self.assertEqual(calculadora.modulo(cor2)[0],7.615773105863909)

    def test_conjugado(self):
        cor1 = [3,21]
        cor2 = [6,-76]
        self.assertEqual(calculadora.conjugado(cor1),[3,-21])
        self.assertEqual(calculadora.conjugado(cor2),[6,76])

    #def test_polarCartesiano(self):

    #def test_cartesianoPolar(self):

    #def test_fase(self):

    
        

if __name__ == "__main__":
    unittest.main()
