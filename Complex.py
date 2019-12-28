import math
import unittest
import random

class Complex():
    
    def __init__(self, real, image):
        self.real = real
        self.image = image

    """
    Module of complex number
    """
    def mdl(self): 
        return math.sqrt(self.real ** 2 + self.image ** 2)
    """
    Complex plane angle
    """
    def trg(self):
        return math.acos(self.real / Complex.mdl(self))
    """
    Conjunction
    """
    def conj(self):
        return Complex(self.real, -self.image)
    """
    Addition
    """
    def __add__(self, other):
        return Complex(self.real + other.real, self.image + other.image)
    """
    Substraction
    """
    def __sub__(self, other):
        return Complex(self.real - other.real, self.image - other.image)
    """
    Multiplication
    """
    def __mul__(self, other):
        return Complex(self.real * other.real - self.image * other.image, self.image * other.real + self.real * other.image)
    """
    Compartition
    """
    def __truediv__(self, other):
        return Complex((self.real*other.real + self.image*other.real)/(other.real ** 2 + other.image ** 2), (self.image *other.real - self.real*other.image)/(other.real ** 2 + other.image ** 2))
    """
    Rising to the power (only real power of numbers)
    """                   
    def __pow__(self, h):
         return Complex(-self.image ** 2 + self.real ** 2, 2 * self.image *self.real)
    """
    Equasion which have this root and conjunction root
    """
    def gleichung(self):
        return('x^2 + ' + str(2 * self.real) +'x + ' + str((Complex.mdl(self)) ** 2))
    """
    Equasion of complex numbers
    """
    def __eq__(self, other):
        if self.real == other.real and self.image == other.image:
            return True
        return False
    
    def __ne__(self, other):
        if self.real != other.real and self.image != other.image:
            return True
        return False
    """
    Right addition
    """
    def __radd__(self, other):
        return Complex(other.real + self.real, other.image + self.image)
    
class CTC(unittest.TestCase): #ComplexTestCase

    def test_add(self):
        c1 = Complex(1, 12)
        c2 = Complex(3,5)
        self.assertEqual(c1 + c2, Complex(4, 17))
        
    def test_equal(self):
        c1 = Complex(1, 12)
        c2 = Complex(1, 12)
        self.assertTrue(c1 == c2)

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
