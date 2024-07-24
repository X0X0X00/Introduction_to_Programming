"""
mkp
"""


from graphics import *

def main():
    win= GraphWin('Trainge',500,500)
    print('Click on Point 1')
    p1 = win.getMouse()
    p1.draw(win)
    print('Click on Point 2')
    p2 = win.getMouse()
    p2.draw(win)
    print('Click on Point 3')
    p3 = win.getMouse()
    p3.draw(win)
    triangle= Polygon(p1,p2,p3)
    triangle.setFill('green')
    triangle.setOutline('cyan')
    triangle.draw(win)
    textlocation= Point(250,480)
    Text(textlocation, 'Click anywhere to quit').draw(win)
    win.getMouse()
    win.close()

main()
