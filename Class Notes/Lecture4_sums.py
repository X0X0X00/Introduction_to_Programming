"""
Write a program to find:

-the sum of the first n natural numbers, where the
value of n is provided by the user.

-the sum of the cubes of the first n natural numbers
where the value of n is provided by the user.
"""


def main():
     n = int(input("n: "))
     sum1 = 0
     sum2 = 0
     for i in range(1,n+1):
          sum1 += i

     for i in range(n+1):
          sum2 += i**3

     print('sum of the first n natural numbers', sum1) 
     print('sum of the cubes of the first n natural numbers', sum2)

main()
