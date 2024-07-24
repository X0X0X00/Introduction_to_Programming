'''
Zhenhao Zhang Homework 2: Numbers. Takes as input Number and output estimated square root of Number
'''



import math


# Defining Function
def secant(x0, x1, Number, Times ):

    global aprox
    count = 1
    for num in range(Times):

        aprox = x0 - (x0 * x0 - Number) / (x0+x1)

        temp = x0
        x0 = aprox
        x1 = temp


        print(count,x0,abs(aprox-math.sqrt(Number)))
        count = count + 1
    return aprox




print("This program calculates the square root of a given number using the secant method.")
Number = eval(input("What is the number for which you want to calculate the square root? "))
Times = eval(input('How many iterations do you want to use? '))

x0 = Number / 5
x1 = Number / 10


# Converting x0 and e to float
x0 = float(x0)
x1 = float(x1)
Number = float(Number)

# Converting N to integer
Times= int(Times)


# Starting Secant Method
secant(x0, x1, Number, Times)


print("My guess for the square root of", Number, "is", aprox)
realresult = math.sqrt(Number)
difference = realresult-aprox
print("The difference between my guess and the real result is", difference)

