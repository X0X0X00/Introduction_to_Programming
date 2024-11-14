from turtle import *

def factorial(n ):
    if n == 0:
        return 1
    else:
        # print(n * factorial(n - 1))
        return n * factorial(n - 1)


def fact_ite(n): # thi is not recursive function. This one uses iteration
    res = 1
    for i in range(1,n+1):
        res = res * i
    return res

def test_fac(m):
    for i in range(m):
        print(factorial(m)==fact_ite(m))

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


"""

for num in range(1,100):
    print(factorial(num ))
        
for num in range(100):
    print('Fib of ', num , ":", fib(num))

"""

def stairs( n ):
    """
    n: int; must be positive
    """
    if n == 1:
        # draw a sinle stair
        forward(20)
        left(90)
        forward(20)
        right(90)
    # elif n == 0:
    #   pass
    elif n > 1:
        forward(20)
        left(90)
        forward(20)
        right(90)
        stairs( n - 1)
        # complete the rest
    
#stairs( 12)

def one_square( size ):
    for i in range(4):
        forward( size)
        left( 90)
        

def squares( size, n ):
    if n == 1:
        one_square( size )
    else:
        one_square( size )
        squares( size/2 , n -1 )
        forward(size)
        left(90)
        forward(size)
        right(90)
        squares( size/2 , n -1 )
        backward(size)
        left(90)
        backward(size)
        right(90)

squares( 100, 5 )
        
        




















        





        
        
    
