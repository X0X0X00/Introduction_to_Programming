"""
week 12 - live coding example
mkp
"""
import math

class Complex:
    def __init__(self,a,b):
        self.re = a
        self.im = b

    def __lt__(self,other):
        return self.re < other.re

    def __add__(self,other):
        return Complex(self.re + other.re, self.im + other.im)

    def info(self):
        print("(",self.re, ',',self.im,')')

    def modulus(self):   #
        return math.sqrt(self.re**2 + self.im**2)
    


if __name__=='__main__':
    n1 = Complex(1,2)
    n2 = Complex(3,5)
    print(n1 < n2)
    n3 =n1+n2
    n3.info()
    print(n3.modulus())


    


