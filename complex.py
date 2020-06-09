import math
import unittest
import random
"""
Complex numbers
"""

class Complex():
    """
    Class of Complex numbers
    """
    
    def __init__(self, real, image):
        self.real = real
        self.image = image

    
    def __abs__(self):
        """
        Module of complex number
        """
        return math.sqrt(self.real ** 2 + self.image ** 2)
    
    def trg(self):
        """
        Complex plane angle
        """
        return math.acos(self.real / Complex.mdl(self))
    
    def conj(self):
        """
        Conjunction
        """
        return Complex(self.real, -self.image)
    
    def __add__(self, other):
        """
        Addition
        """
        return Complex(self.real + other.real, self.image + other.image)
    
    def __sub__(self, other):
        """
        Substraction
        """
        return Complex(self.real - other.real, self.image - other.image)
    
    def __mul__(self, other):
        """
        Multiplication
        """
        return Complex(self.real * other.real - self.image * other.image, self.image * other.real + self.real * other.image)
    
    def __truediv__(self, other):
        """
        Compartition
        """
        return Complex((self.real*other.real + self.image*other.real)/(other.real ** 2 + other.image ** 2), (self.image *other.real - self.real*other.image)/(other.real ** 2 + other.image ** 2))
                       
    def __pow__(self, h):
        """
        Rising to the power (only real power of numbers)
        """
        return Complex(-self.image ** 2 + self.real ** 2, 2 * self.image *self.real)
    
    def gleichung(self):
        """
        Equasion which have this root and conjunction root
        """
        return('x^2 + ' + str(2 * self.real) +'x + ' + str((Complex.mdl(self)) ** 2))
    
    def __eq__(self, other):
        """
        Equasion of complex numbers
        """
        if self.real == other.real and self.image == other.image:
            return True
        return False
    
    def __ne__(self, other):
        if self.real != other.real and self.image != other.image:
            return True
        return False
    
    def __radd__(self, other):
        """
        Right addition
        """
        return Complex(other.real + self.real, other.image + self.image)

    def __str__(self):
        """
        form of complex number
        """
        returnstr(self.real) +  ' + i' + str(self.image)
class CTC(unittest.TestCase): #ComplexTestCase
    """
    Test for class check
    """
    def test_add(self):
        c1 = random.randint(-100, 100)
        c2 = random.randint(-100, 100)
        c3 = random.randint(-100, 100)
        c4 = random.randint(-100, 100)
        self.assertEqual(Complex(c1, c2) + Complex(c3, c4), Complex(c1 + c3, c2 + c4))
        
    def test_equal(self):
        c1 = random.randint(-100, 100)
        c2 = random.randint(-100, 100)
        self.assertTrue(Complex(c1, c2) == Complex(c1, c2))

    def test_power(self):
        h1 = Complex(1, 5)
        h2 = Complex(2, 0)
        self.assertEqual(h1 ** h2, Complex(-24, 10))

    def test_truediv(self):
        h1 = Complex(2, 4)
        h2 = Complex (1, 1)
        self.assertEqual(h1 / h2, Complex(3, 1))
        
if __name__ == '__main__':
    unittest.main()      
