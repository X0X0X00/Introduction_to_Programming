"""
quadratics.py
A program that computes the real roots of a quadratic equation.
Illustrates use of the math library.
Note: This program crashes if the equation has no real roots.
"""


import math # Makes the math library available.

def quadriatic(a,b,c):
     discRoot  = b*b-4*a*c
     if discRoot  > 0:
          root1 = (-b + math.sqrt(discRoot))/(2 * a)
          root2 = (-b - math.sqrt(discRoot))/(2 * a)
          print('Solutions are:' , root1, ' ', root2)
     elif discRoot == 0:
          root = (-b)/(2 * a)
          print('One solution: ', root)
     else:
          print('No solutions')

     
     
if __name__=='__main__':
     print("This program finds the real solutions to a quadratic")
     print()
     a = float(input("Enter coefficient a: ") )
     b = float(input("Enter coefficient b: ") )
     c = float(input("Enter coefficient c: ") )
     quadriatic(a,b,c)


