"""
week 6 to be completed on Wednesday
mkp
"""


from turtle import *
import math

def initialize():
    up()
    backward(200)
    right(90)
    forward(200)
    left(90)
    down()

def frame():
    for i in range(4):
        forward(400)
        left(90)

def door():
    up()
    forward(150)
    down()
    for i in range(2):
        forward(100)
        left(90)
        forward(150)
        left(90)
    up()
    backward(150)

def window():
    down()
    for i in range(4):
        forward(100)
        left(90)
    up()

def windows():
    up()
    left(90)
    forward(50)
    right(90)
    forward(25)
    window()
    forward(250)
    window()
    
    
    
def main():
    initialize()
    frame()
    door()
    windows()


main()
