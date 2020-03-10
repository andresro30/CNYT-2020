import unittest
import calculadora,simulaciones
import math


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

    def test_sumaVectores(self):
        ans1 = calculadora.sumaVectores([(1,2),(1,2),(3,5)],[(-2,2),(2,2),(4,10)])
        ans2 = calculadora.sumaVectores([(1,0),(1,-2),(3,2)],[(2,2),(3,2),(4,5)])
        self.assertEqual(ans1,[(-1,4),(3,4),(7,15)])
        self.assertEqual(ans2,[(3,2),(4,0),(7,7)])
        
    def test_inversaVector(self):
        ans1 = calculadora.inversaVector([(1,-1),(2,3),(-1,3)])
        ans2 = calculadora.inversaVector([(1,2),(-3,3),(-1,3)])
        self.assertEqual(ans1,[(-1,1),(-2,-3),(1,-3)])
        self.assertEqual(ans2,[(-1,-2),(3,-3),(1,-3)])
        
    def test_multiplicacionVectores(self):
        ans1 = calculadora.multiplicacionVectores([(1,2),(3,4),(1,5)],(0,0))
        ans2 = calculadora.multiplicacionVectores((1,1),[(1,2),(3,4),(1,5)])
        self.assertEqual(ans1,[(0,0),(0,0),(0,0)])
        self.assertEqual(ans2,[(-1,3),(-1,7),(-4,6)])

    def test_sumaMatrices(self):
        ans1 = calculadora.sumaMatrices([[(1,1),(2,-3)],[(4,2),(2,4)]],[[(1,0),(1,0)],[(1,0),(1,0)]])
        ans2 = calculadora.sumaMatrices([[(1,3),(2,3)],[(1,3),(2,3)]],[[(1,0),(3,6)],[(1,0),(3,6)]])
        self.assertEqual(ans1,[[(2,1),(3,-3)],[(5,2),(3,4)]])
        self.assertEqual(ans2,[[(2,3),(5,9)],[(2,3),(5,9)]])

    def test_inversaMatriz(self):
        ans1 = calculadora.inversaMatriz([[(1,1),(2,-3)],[(4,2),(2,4)]])
        ans2 = calculadora.inversaMatriz([[(1,1),(0,3)],[(-1,2),(-2,4)]])
        self.assertEqual(ans1,[[(-1,-1),(-2,3)],[(-4,-2),(-2,-4)]])
        self.assertEqual(ans2,[[(-1,-1),(0,-3)],[(1,-2),(2,-4)]])

    def multiplicacionEscalarMatrices(self):
        ans1 = calculadora.multiplicacionEscalarMatrices([[(1,1),(2,-3)],[(4,2),(2,4)]],(1,1))
        ans2 = calculadora.multiplicacionEscalarMatrices([[(1,1),(2,-3)],[(4,2),(2,4)]],(2,3))
        self.assertEqual(ans1,[[(0,2),(5,-1)],[(2,6),(-2,6)]])
        self.assertEqual(ans2,[[(-1,5),(13,0)],[(2,16),(-8,14)]])

    def test_traspuesta(self):
        ans1 = calculadora.traspuesta([[(1,1),(2,-3)],[(4,2),(2,4)]])
        ans2 = calculadora.traspuesta([[(1,1),(2,-3),(5,4)],[(4,2),(2,4),(4,5)]])
        self.assertEqual(ans1,[[(1,1),(4,2)],[(2,-3),(2,4)]])
        self.assertEqual(ans2,[[(1,1),(4,2)],[(2,-3),(2,4)],[(5,4),(4,5)]])

    def test_conjugadoVector(self):
        ans1 = calculadora.conjugadoVector([(1,2),(1,-2),(1,5)])
        ans2 = calculadora.conjugadoVector([(1,3),(3,2),(3,-9)])
        self.assertEqual(ans1,[(1,-2),(1,2),(1,-5)])
        self.assertEqual(ans2,[(1,-3),(3,-2),(3,9)])

        

    def test_conjugadoMatriz(self):
        ans1 = calculadora.conjugadoMatriz([[(1,2),(2,1)],[(1,-2),(2,-3)],[(3,4),(3,-1)]])
        ans2 = calculadora.conjugadoMatriz([[(1,1),(2,2),(1,1)],[(2,2),(3,-3),(2,3)]])
        self.assertEqual(ans1,[[(1,-2),(2,-1)],[(1,2),(2,3)],[(3,-4),(3,1)]])
        self.assertEqual(ans2,[[(1,-1),(2,-2),(1,-1)],[(2,-2),(3,3),(2,-3)]])

    def test_matrizAdjunta(self):
        ans1 = calculadora.matrizAdjunta([[(1,1),(2,-3)],[(4,2),(2,4)]])
        ans2 = calculadora.matrizAdjunta([[(1,1),(2,3)],[(4,2),(1,4)],[(1,0),(3,-4)]])
        self.assertEqual(ans1,[[(1,-1),(4,-2)],[(2,3),(2,-4)]])
        self.assertEqual(ans2,[[(1,-1),(4,-2),(1,0)],[(2,-3),(1,-4),(3,4)]])

    def test_productoVectorMatriz(self):
        ans1 = calculadora.productoVectorMatriz([(1,1),(2,3)],[[(1,2),(2,1)],[(3,3),(1,-2)]])
        ans2 = calculadora.productoVectorMatriz([(0,0),(0,0)],[[(1,2),(2,1)],[(3,3),(1,-2)]])
        self.assertEqual(ans1,[(0,11),(8,5)])
        self.assertEqual(ans2,[(0,0),(0,0)])

    def test_productoInternoVectores(self):
        ans1 = calculadora.productoInternoVectores([(1,0),(0,1),(1,-3)],[(2,1),(0,1),(2,0)])
        ans2 = calculadora.productoInternoVectores([(1,-2),(-2,1),(4,3)],[(2,1),(1,-3),(3,0)])
        self.assertEqual(ans1,(5,7))
        self.assertEqual(ans2,(7,1))

    def test_normaMatriz(self):
        self.assertEqual(calculadora.normaVector([(3,0),(-6,0),(-2,0)]),7.0)
        self.assertEqual(calculadora.normaVector([(2,0),(4,0)]),4.47213595499958)
        self.assertEqual(calculadora.normaVector([(4,0),(3,0)]),5.0)

    def test_distanciaVectores(self):
        ans1 = calculadora.distanciaVectores([(0,0),(0,0)],[(1,1),(2,4)])
        ans2 = calculadora.distanciaVectores([(1,2),(2,5)],[(2,6),(5,3)])
        self.assertEqual(ans1,4.69041575982343)
        self.assertEqual(ans2,5.477225575051661)
        

    
    def test_esUnitaria(self):
        self.assertFalse(calculadora.esUnitaria([[(1,1),(0,0)],[(0,0),(1,-1)]]))
        self.assertFalse(calculadora.esUnitaria([[(-1,0),(0,-1)],[(0,1),(1,0)]]))
        self.assertTrue(calculadora.esUnitaria([[(0,0),(1,0)],[(1,0),(0,0)]]))
        
    def test_esHermitiana(self):
        self.assertFalse(calculadora.esHermitiana([[(1,1),(0,0)],[(0,0),(1,-1)]]))
        self.assertTrue(calculadora.esHermitiana([[(-1,0),(0,-1)],[(0,1),(1,0)]]))
        self.assertTrue(calculadora.esUnitaria([[(0,0),(1,0)],[(1,0),(0,0)]]))

    def test_productoTensorVectores(self):
        ans1 = calculadora.productoTensorVectores([(-1,0),(2,0),(5,0)],[(4,0),(-3,0)])
        ans2 = calculadora.productoTensorVectores([(-1,1),(2,-1),(5,1)],[(4,1),(3,0)])
        self.assertEqual(ans1,[(-4,0),(3,0),(8,0),(-6,0),(20,0),(-15,0)])
        self.assertEqual(ans2,[(-5,3),(-3,3),(9,-2),(6,-3),(19,9),(15,3)])
        

    def test_productoTensorMatrices(self):
        ans1 = calculadora.productoTensorMatrices([[(1,0),(2,0)],[(0,0),(1,0)]],[[(3,0),(2,0)],[(-1,0),(0,0)]])
        ans2 = calculadora.productoTensorMatrices([(0,0),(0,0)],[[(1,0),(2,0)],[(3,0),(2,0)],[(1,1),(2,2)]])
        self.assertEqual(ans1,[[(3,0),(2,0),(6,0),(4,0)],[(-1,0),(0,0),(-2,0),(0,0)],[(0,0),(0,0),(3,0),(2,0)],[(0,0),(0,0),(-1,0),(0,0)]])
        self.assertEqual(ans2,[[(0,0),(0,0),(0,0),(0,0)],[(0,0),(0,0),(0,0),(0,0)],[(0,0),(0,0),(0,0),(0,0)]])


    """  Test de Simulaciones """

    def test_canicasBooleanas(self):
        estado = [6,2,1,5,3,10]
        inicial = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,0,0,0,1],[0,0,0,1,0,0],[0,0,1,0,0,0],[1,0,0,0,1,0]]
        ans = simulaciones.canicasBooleanas(estado,inicial,1)
        ans2 = simulaciones.canicasBooleanas(estado,inicial,2)
        ans3 = simulaciones.canicasBooleanas(estado,inicial,5)
        self.assertEqual(ans,[0,0,12,5,1,9])
        self.assertEqual(ans2,[0,0,9,5,12,1])
        self.assertEqual(ans3,[0,0,9,5,12,1])

    def test_rendijaProbabilistica(self):
        unmedio = 1/2
        untercio = 1/3
        inicial = [[0,0,0,0,0,0,0,0],[unmedio,0,0,0,0,0,0,0],[unmedio,0,0,0,0,0,0,0],[0,untercio,0,1,0,0,0,0],[0,untercio,0,0,1,0,0,0],
           [0,untercio,untercio,0,0,1,0,0],[0,0,untercio,0,0,0,1,0],[0,0,untercio,0,0,0,0,1]]

        ans = simulaciones.rendijaProbabilistica(2,8,inicial,[1,0,0,0,0,0,0,0])
        ans3 = simulaciones.rendijaProbabilistica(2,10,inicial,[1,0,0,0,0,0,0,0])

        self.assertEqual(ans,[0.0, 0.0, 0.0, 0.16666666666666666, 0.16666666666666666, 0.3333333333333333, 0.16666666666666666, 0.16666666666666666])
        self.assertEqual(ans3,"La matriz de probabilidades debe ser proporcional a los objetivos")

    def test_rendijaCuantica(self):
        estado =  mat = [[(0,0),(0,0),(1,2),(1,2)],[(0,0),(1,2),(0,0),(1,2)],[(0,0),(1,2),(1,2),(0,0)],[(0,0),(0,0),(1,2),(1,2)]]
        ans = simulaciones.rendijaCuantica(2,4,estado,[(0,0),(1,2),(1,2),(0,0)])
        self.assertEqual(ans,[(451, -418), (451, -418), (410, -380), (451, -418)])
        
if __name__ == "__main__":
    unittest.main()
