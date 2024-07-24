from graphics import *

def question1():
    win = GraphWin()
    p1 = win.getMouse()
    p2 = win.getMouse()
    Rectangle(p1,p2).draw(win)
    a = abs(p1.getY()- p2.getY())
    b = abs(p1.getX() -p2.getX())
    print(a*b)
    
    


def question2(k):
    sum = 0
    for i in range(1,k+1):
        sum = sum + 1/i
    return sum

print(question2(3))

def question3(file):
    sum = 0
    for line in file:
        for ch in line:
            if ch == 'b':
                sum = sum + 1
    return sum

def question2_alt(file):
    list_of_lines = file.readlines()
    for line in list_of_lines:
        for ch in line:
            if ch == 'b':
            sum = sum + 1
    return sum

def sum_if_even(a,b,c):
    sum= 0
    if a % 2 == 0:
        sum = sum +a
    if b % 2 == 0:
        sum = sum +b
    if c % 2 == 0:
        sum = sum +c
    return sum
        
            


        







    
    
    
