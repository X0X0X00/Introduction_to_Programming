"""
quadratics.py
A program that computes the real roots of a quadratic equation.
Illustrates use of the math library.
Note: This program crashes if the equation has no real roots.
"""


import math # Makes the math library available.

def quadriatic(a,b,c):
     discRoot = math.sqrt(b*b-4*a*c)
     root1 = (-b + discRoot)/(2 * a)
     root2 = (-b - discRoot)/(2 * a)
     return root1, root2
     
     
def main() :
     print("This program finds the real solutions to a quadratic")
     print()
     a = float(input("Enter coefficient a: ") )
     b = float(input("Enter coefficient b: ") )
     c = float(input("Enter coefficient c: ") )
     rt1, rt2  = quadriatic(a,b,c)
     print("The solutions are: ", rt1, rt2 )

main()
