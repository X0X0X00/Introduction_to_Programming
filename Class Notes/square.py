"""
square.py
CSC 161 Lecture 2 - Example 2
Author: MKP
"""


import turtle

def main():
    side = eval(input("Side size: "))
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)

main()
