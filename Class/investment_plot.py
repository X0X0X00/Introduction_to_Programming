"""
Sudocode
For successive years 1 through 10 
    Calculate principal = principal * (1 + apr) 
    Draw a bar for this year having a height corresponding to principal 
Wait for user to press Enter .
"""
from graphics import *

# this code from week 3

def main():
    win = GraphWin("Investment growth chart",320 , 240) # druga wysokosc
    
    #win.setCoords(-1.75,-200 , 11.5, 10400)
    #Text(Point(160 , 120) , ' center').draw(win)
    Text(Point(20 , 230) , ' 0.0K').draw(win) 
    Text(Point(20 , 180) , ' 2.5K').draw(win) 
    Text(Point(20 , 130) , ' 5.0K').draw(win) 
    Text(Point(20 , 80) , ' 7.5K').draw(win) 
    Text(Point(20 , 30) , ' 10.0K').draw(win)
    intrest = eval(input('Intrest as 0.1 for 10%: '))
    money = int(input("Initial capital: "))
    height = money * 0.02 
    bar = Rectangle(Point (40 , 230) , Point (65 , 230-height) ) 
    bar.setFill( "green") 
    bar.setWidth(2) 
    bar.draw(win)
    for year in range(10):
        money = money + intrest*money
        print(money)
        xll = year * 25 + 40 
        height = money * 0.02
        # In drawing the scale, we determined that 100 pixels is equal to $5,000. This 
        # means that we have 100/5000 = 0.02 pixels to the dollar. 
        bar = Rectangle(Point (xll , 230) , Point(xll+25 , 230-height)) 
        bar.setFill( "green") 
        bar.setWidth(2) 
        bar.draw(win) 
        
    input( "Press <Enter> to quit ") 
    win.close ()    

main()




# create a default 200x200 window 
win = GraphWin( "Tic-Tac-Toe ") 
# set coordinates to go from (0 , 0) in the lower left 
# to (3 , 3) in the upper right . 
win . setCoords (0.0, 0.0, 3.0, 3.0) 
# Draw vertical lines 
Line (Point ( 1 , 0) , Point ( 1 , 3)) .draw(win) 
Line (Point (2,0) , Point (2,3)) .draw(win) 
# Draw horizontal lines 
Line (Point (0,1 ) , Point (3,1 )) .draw(win) 
Line (Point (0,2) , Point (3,2)) .draw(win)




# click . py 
from graphics import * 
def main() : 
    win = GraphWin("Click Me ! ") 
    for i in range(10) : 
        p = win.getMouse () 
        print( "You clicked at :", p.getX() , p.getY() ) 
main()






