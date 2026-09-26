import unittest
from calculadora import sumar, restar, multiplicar, dividir


class TestCalculadora(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(10, 5), 15)

    def test_restar(self):
        self.assertEqual(restar(10, 5), 5)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(10, 5), 50)

    def test_dividir(self):
        self.assertEqual(dividir(10, 5), 2)

    def test_division_entre_cero(self):
        with self.assertRaises(ValueError):
            dividir(10, 0)


if __name__ == "__main__":
    unittest.main()