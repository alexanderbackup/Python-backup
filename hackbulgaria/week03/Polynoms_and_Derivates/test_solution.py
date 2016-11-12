from solution import PolynomsAndDerivates, CalculatePolynoms
import unittest

class TestPolynomsAndDerivates(unittest.TestCase):
    def setUp(self):
        self.polynom = PolynomsAndDerivates('2x^3+x')
        self.derivative = CalculatePolynoms('2x^3+x^2+10x^2+2x+1')

    def test_highest_degree(self):
        self.assertEqual(self.polynom.highest_degree(), 
                         [('2x^3', 3), ('x', 1)])

    def test_repr_derivative(self):
        self.polynom.highest_degree()
        self.assertEqual(self.polynom.repr_derivative(), 
                        'The derivative of f(x) = 2*x^3 + x is:')
    
    def test_placing_stars(self):
        self.assertEqual(self.polynom.placing_stars(('10x^3', 3)), '10*x^3')

    def test_calculate_derivative(self):
        self.assertEqual(self.derivative.calculate_derivative(),
                         [('2x^3', 3), ('11x^2', 2), ('2x', 1), ('1', 0)])

    def test_repr_calculated_derivative(self):
        self.derivative.calculate_derivative()
        self.assertEqual(self.derivative.repr_calculated_derivative(),
                         "f'(x) = 6*x^2 + 22x + 2")

if __name__ == '__main__':
    unittest.main()
