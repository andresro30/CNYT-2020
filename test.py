import unittest
import Complex


class Test(unittest.TestCase):

    def testSuma(self):
        cor1 = [4,6]
        cor2 = [1,-5]
        ans = Complex.suma(cor1,cor2)
        self.assertEquals(ans,[5,1])


    if __name__ == '__main__':
        unittest.main()
