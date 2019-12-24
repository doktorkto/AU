{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "import math\n",
    "\n",
    "class Complex():\n",
    "    \n",
    "    def __init__(self, real, image):\n",
    "        self.real = real\n",
    "        self.image = image\n",
    "    def mdl(self): #module of complex number\n",
    "        return math.sqrt(self.real ** 2 + self.image)\n",
    "    \n",
    "    def trg(self): #angle phi\n",
    "        return math.acos(self.real / Complex.mdl(self))\n",
    "    \n",
    "    def conj(self): #conjunction\n",
    "        return Complex(self.real, -self.image)\n",
    "    \n",
    "    def __add__(self, other):\n",
    "        return Complex(self.real + other.real, self.image + other.image)\n",
    "    \n",
    "    def __sub__(self, other):\n",
    "        return Complex(self.real - other.real, self.image - other.image)\n",
    "    \n",
    "    def __mul__(self, other):\n",
    "        return Complex(self.real * other.real - self.image * other.image, self.image * other.real + self.real * other.image)\n",
    "    \n",
    "    def __truediv__(self, other):\n",
    "        return Complex((self.real * other.real - self.image * other.image)/Complex.mdl(other) ** 2 , (self.real * other.image + self.image * other.real)/Complex.mdl(other) ** 2)\n",
    "    \n",
    "    def __pow__(self, h): #with complex power\n",
    "         return Complex(math.cos(Complex.trg(self) * h.real) * math.exp(-Complex.trg(self) * h.image), math.sin(Complex.trg(self) * h.real) * math.exp(-Complex.trg(self) * h.image))\n",
    "    \n",
    "    def gleichung(self): #fiding the equasion which have this root\n",
    "        return('x^2 + ' + str(2 * self.real) +'x + ' + str((Complex.mdl(self)) ** 2))\n",
    "    \n",
    "    def __eq__(self, other):\n",
    "        if self.real == other.real and self.image == other.image:\n",
    "            return true\n",
    "        return false\n",
    "    \n",
    "    def __radd__(self, other):\n",
    "        return Complex(other.real + self.real, other.image + self.image)\n",
    "    \n",
    "def intoComplex(x):\n",
    "    return complex(x, 0)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
