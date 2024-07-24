# Zhenhao Zhang 9/27/23


## First Version

from graphics import *


def draw_house():

    ## Part 1
    # Create a window with title "House" and dimensions 500x500
    win = GraphWin("House",500,500)


    # Prompt for the first click
    # print("Click on lower left corner of the house frame.") # Test
    text = Text(Point(250,20),"Click on lower left corner of the house frame.")
    text.draw(win)
    p1 = win.getMouse()
    text.undraw()

    # Test
    # Draw a circle at the first click point
    # circle1 = Circle(p1, 5)  # 5 is the radius of the circle
    # circle1.setFill('red')
    # circle1.draw(win)

    # Prompt for the second click
    # print("Click on upper right corner of the house frame.") # Test
    text = Text(Point(250,20),"Click on upper right corner of the house frame.")
    text.draw(win)
    p2 = win.getMouse()
    text.undraw()

    # Test
    # Draw a circle at the second click point
    # circle2 = Circle(p2, 5)
    # circle2.setFill('red')
    # circle2.draw(win)

    # Draw the frame of the house
    frame = Rectangle(p1,p2)
    frame.draw(win)

    ## Part 2
    # Prompt for the third click
    # print("Click on the center of the top of the door") # Test
    text = Text(Point(250,20),"Click on the center of the top of the door")
    text.draw(win)
    p3 = win.getMouse()
    text.undraw()

    # Draw the door
    door_width = abs(p2.getX() - p1.getX()) / 5
    door = Rectangle(Point(p3.getX() - door_width / 2, p3.getY()),
                     Point(p3.getX() + door_width / 2, p1.getY()))
    door.draw(win)

    # Calculate the position for the doorknob
    doorknob_x = p3.getX() + door_width / 2 - 10  # 10 units from the right edge of the door
    doorknob_y = (p3.getY() + p1.getY()) / 2  # Half the height of the door

    # Draw the doorknob
    doorknob = Circle(Point(doorknob_x, doorknob_y), 5)  # 5 is the radius of the doorknob
    doorknob.setFill('yellow')  # Set the color of the doorknob to yellow
    doorknob.draw(win)

    # Test
    # Draw a circle at the third click point
    # circle3 = Circle(p3, 5)
    # circle3.setFill('red')
    # circle3.draw(win)

    ## Part 3
    # Prompt for the fourth click
    # print("Click on the center of the window.") # Test
    text = Text(Point(250, 20), "Click on the center of the window.")
    text.draw(win)
    p4 = win.getMouse()  # Fourth click
    text.undraw()

    # Test
    # Draw a circle at the fourth click point
    # circle4 = Circle(p4, 5)
    # circle4.setFill('red')
    # circle4.draw(win)

    # Calculate the width of the window as 3/4 of the width of the door
    window_width = (3 / 4) * door_width

    # Draw the window
    window = Rectangle(Point(p4.getX() - window_width / 2, p4.getY() - window_width / 2),
                       Point(p4.getX() + window_width / 2, p4.getY() + window_width / 2))
    window.draw(win)

    # Draw the window's muntins
    muntin1 = Line(Point(p4.getX(), p4.getY() - window_width / 2),
                   Point(p4.getX(), p4.getY() + window_width / 2))
    muntin1.draw(win)
    muntin2 = Line(Point(p4.getX() - window_width / 2, p4.getY()),
                   Point(p4.getX() + window_width / 2, p4.getY()))
    muntin2.draw(win)

    ## Part 4
    # Prompt for the fifth click
    text = Text(Point(250, 20), "Click on the peak of the roof.")
    text.draw(win)
    p5 = win.getMouse()  # Fifth click
    text.undraw()

    # Draw a circle at the fifth click point
    # circle5 = Circle(p5, 5)
    # circle5.setFill('red')
    # circle5.draw(win)

    # Draw the roof
    roof_side1 = Line(p5, Point(p1.getX(), p2.getY()))  # From peak to upper left corner of the frame
    roof_side1.draw(win)
    roof_side2 = Line(p5, Point(p2.getX(), p2.getY()))  # From peak to upper right corner of the frame
    roof_side2.draw(win)

    ## part 5
    # Waiting for another click to exit
    text = Text(Point(250,20),"Click anywhere to close")
    text.draw(win)
    win.getMouse()
    win.close()


draw_house()


## Version 2

# from graphics import *
#
# def draw_house():
#     # Create a window with title "House" and dimensions 500x500
#     win = GraphWin("House", 500, 500)
#
#     # Create a Text object for displaying prompts
#     prompt = Text(Point(250, 20), "")
#     prompt.draw(win)
#
#     # Prompt for the first click
#     prompt.setText("Click on lower left corner of the house frame.")
#     p1 = win.getMouse()  # First click
#
#     # Prompt for the second click
#     prompt.setText("Click upper right corner of the house frame.")
#     p2 = win.getMouse()  # Second click
#
#     # Draw the frame of the house
#     frame = Rectangle(p1, p2)
#     frame.draw(win)
#
#     # Calculate the width of the house frame
#     frame_width = p2.getX() - p1.getX()
#     # Calculate the width of the door as 1/5 of the width of the house frame
#     door_width = frame_width / 5
#
#     # Prompt for the third click
#     prompt.setText("Click on the center of the top edge of the door.")
#     p3 = win.getMouse()  # Third click
#
#     # Draw the door
#     door = Rectangle(Point(p3.getX() - door_width / 2, p3.getY()),
#                      Point(p3.getX() + door_width / 2, p1.getY()))
#     door.draw(win)
#
#     # Calculate the position for the doorknob
#     doorknob_x = p3.getX() + door_width / 2 - 10
#     doorknob_y = (p3.getY() + p1.getY()) / 2
#
#     # Draw the doorknob
#     doorknob = Circle(Point(doorknob_x, doorknob_y), 5)
#     doorknob.setFill('yellow')
#     doorknob.draw(win)
#
#     # Prompt for the fourth click
#     prompt.setText("Click on the center of the window.")
#     p4 = win.getMouse()  # Fourth click
#
#     # Calculate the width of the window as 3/4 of the width of the door
#     window_width = (3 / 4) * door_width
#
#     # Draw the window
#     window = Rectangle(Point(p4.getX() - window_width / 2, p4.getY() - window_width / 2),
#                        Point(p4.getX() + window_width / 2, p4.getY() + window_width / 2))
#     window.draw(win)
#
#     # Draw the window's muntins
#     muntin1 = Line(Point(p4.getX(), p4.getY() - window_width / 2),
#                    Point(p4.getX(), p4.getY() + window_width / 2))
#     muntin1.draw(win)
#     muntin2 = Line(Point(p4.getX() - window_width / 2, p4.getY()),
#                    Point(p4.getX() + window_width / 2, p4.getY()))
#     muntin2.draw(win)
#
#     # Prompt for the fifth click
#     prompt.setText("Click on the peak of the roof.")
#     p5 = win.getMouse()  # Fifth click
#
#     # Draw the roof
#     roof_side1 = Line(p5, Point(p1.getX(), p2.getY()))
#     roof_side1.draw(win)
#     roof_side2 = Line(p5, Point(p2.getX(), p2.getY()))
#     roof_side2.draw(win)
#
#     # Final prompt
#     prompt.setText("Click anywhere to close.")
#     win.getMouse()
#     win.close()
#
# # Uncomment the below line to run the function
# draw_house()




