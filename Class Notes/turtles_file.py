"""
mkp
"""
from turtle import *
import math


tina = Turtle()
tom = Turtle()
tara= Turtle()
ted = tina.clone()

tina.shape('turtle')
tom.shape('turtle')
tara.shape('turtle')
ted.shape('turtle')

# relocate turtles
tom.up()
tom.backward(200)
tom.down()

tara.up()
tara.right(90)
tara.forward(200)
tara.left(90)
tara.down()

ted.up()
ted.backward(200)
ted.right(90)
ted.forward(200)
ted.left(90)
ted.down()

tina.color('red')
tom.color('yellow')
tara.color('blue')
ted.color('green')

tina.speed(0)
tom.speed(0)
ted.speed(0)
tara.speed(0)

def main():
     distance = 200
     for i in range(20):
          tina.forward(distance)
          tina.left(90)
          tom.forward(distance)
          tom.left(90)
          tara.forward(distance)
          tara.left(90)
          ted.forward(distance)
          ted.left(90)
          distance = distance - 10
          

main()







