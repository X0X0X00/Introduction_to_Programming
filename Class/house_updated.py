"""
week 6 updated
mkp
"""


from turtle import *
import math

def initialize():
    speed(0)
    screen = Screen()
    screen.setup(1000,1000)
    up()
    backward(200)
    right(90)
    forward(300)
    left(90)
    down()

def frame():
    """
    pre-conditions: lower left corner of the house
    post-conditions: lower left corner of the house
    """
    for i in range(4):
        forward(400)
        left(90)

def roof():
    """
    pre-conditions: lower left corner of the house
    post-conditions: lower left corner of the house
    """
    down()
    left(90)
    forward(400)
    right(45)
    forward(200*math.sqrt(2))
    right(90)
    forward(200*math.sqrt(2))
    left(45)
    backward(400)
    right(90)
    forward(400)
    left(90)

    
def door():
    """
    pre-conditions: lower left corner of the house
    post-conditions: lower left corner of the house
    """
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
    fillcolor('SkyBlue')
    begin_fill()
    for i in range(4):
        forward(100)
        left(90)
    end_fill()
    up()

def windows():
    """
    pre-conditions: lower left corner of the house
    post-conditions: lower left corner of the house
    """
    up()
    left(90)
    forward(50)
    right(90)
    forward(25)
    window()
    forward(250)
    window()
    backward(275)
    right(90)
    forward(50)
    left(90)
    
    
    
def main():
    initialize()
    frame()
    door()
    roof()
    windows()



main()
