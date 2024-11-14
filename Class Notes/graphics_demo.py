"""
mkp
graphics demo week 4

"""

from graphics import *

win = GraphWin('Graphics Demo',500,500)
p = Point(50,60)
p.draw(win)

x = p.getX()
y = p.getY()
print("x:", x, "y", y)

stop1=input('Press Enter to continue')

center = Point(100,100)
circ = Circle(center, 30)
circ.draw(win)
circ.setFill('red')

label = Text(center, "Red Circle")
label.draw(win)

line = Line(Point(20,30), Point(180, 165))
line.draw(win)

stop2=input('Press Enter to continue')

for i in range(10):
     stop=input('Press Enter to continue')
     circ.move(50,0)





