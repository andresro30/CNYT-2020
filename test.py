import unittest
import calculadora


class TestCalculadora(unittest.TestCase):

    def test_suma(self):
        ans1 = calculadora.suma((4,6),(1,-5))
        ans2 = calculadora.suma((76,23),(-80,30))
        ans3 = calculadora.suma((50,6),(18,-5))
        self.assertEqual(ans1,(5,1))
        self.assertEqual(ans2,(-4,53))
        self.assertEqual(ans3,(68,1))
        
    def test_resta(self):
        ans1 = calculadora.resta((4,18),(1,-5))
        ans2 = calculadora.resta((50,6),(18,-5))
        ans3 = calculadora.resta((45,15),(18,5))
        self.assertEqual(ans1,(3,23))
        self.assertEqual(ans2,(32,11))
        self.assertEqual(ans3,(27,10))

    def test_multiplicacion(self):
        ans = calculadora.multiplicacion((4,6),(1,4))
        self.assertEqual(ans,(-20,22))

    def test_division(self):
        ans = calculadora.division((3,2),(1,-2))
        self.assertEqual(ans,(-0.2,1.6))

    def test_modulo(self):
        self.assertEqual(calculadora.modulo((1,5))[0],5.0990195135927845)
        self.assertEqual(calculadora.modulo((3,7))[0],7.615773105863909)
        self.assertEqual(calculadora.modulo((4,4))[0],5.656854249492381)

    def test_conjugado(self):
        self.assertEqual(calculadora.conjugado((3,21)),(3,-21))
        self.assertEqual(calculadora.conjugado((6,-76)),(6,76))
        self.assertEqual(calculadora.conjugado((5,16)),(5,-16))

    def test_polarCartesiano(self):
        self.assertEqual(calculadora.polarCartesiano((13,23)),(11.966563094881725,5.079504670360558))
        self.assertEqual(calculadora.polarCartesiano((2,120)),(-0.9999999999999996,1.7320508075688774))
        self.assertEqual(calculadora.polarCartesiano((1,0)),(1,0))
        
    def test_cartesianoPolar(self):
        self.assertEqual(calculadora.cartesianoPolar((1,2)),(2.23606797749979,63.43494882292201))
        self.assertEqual(calculadora.cartesianoPolar((-3,1)),(3.1622776601683795,18.43494882292201))
        self.assertEqual(calculadora.cartesianoPolar((2,2)),(2.8284271247461903,45.0))

    def test_fase(self):
        self.assertEqual(calculadora.fase((3,21))[0],1.4288992721907328)
        self.assertEqual(calculadora.fase((6,-76))[0],-1.492012365805753)
        self.assertEqual(calculadora.fase((5,16))[0],1.2679114584199251)


    """ Operaciones de Vectores y Matrices Complejas"""
    

    def simulacionQuantica(self):
        r2 = math.sqrt(2)
        H = [[(r2,0),(r2,0)],[(r2,0),(r2*-1,0)]]
        
        X = [[(0,0),(1,0)],[(1,0),(0,0)]]
        base = [(1,0),(0,0),(0,0),(0,0)]
        M1 = productoTensorMatrices(H,H)
        M2 = productoTensorMatrices(H,X)
        M3 = multiplicarMatrices(M2,M1)

        producto = multiplicarMatrices(M2,M1)
        op = productoVectorMatriz(base,producto)
        print(op)

        
        


        

if __name__ == "__main__":
    unittest.main()
