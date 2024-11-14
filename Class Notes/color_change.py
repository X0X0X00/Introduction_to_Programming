import graphics


win = graphics.GraphWin()



def color_change(object, color):
    object.setFill(color)


def ask_user(object, x):
    for i in range(5):
        x = x + 1 
        color = input('Color: ')
        color_change(object, color)
    return x

def main():
    p1= graphics.Point(100,100)
    cir= graphics.Circle(p1, 20)
    cir.draw(win)
    x = 5
    #color_change(cir, 'blue') <--- can be removed
    x = ask_user(cir, x)
    print(x)

main()



