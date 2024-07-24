
"""  Zhenhao Zhang 12/3/23 """


import turtle


def init(size):
    turtle.reset()
    turtle.setup(600, 600)  # 设置窗口尺寸
    turtle.setworldcoordinates(-size, -size, 2 * size, size)  # 设置世界坐标
    turtle.speed(0)
    turtle.up()  # 抬起画笔
    turtle.pensize(2)


def one_rectangle(x, y, length, width):
    turtle.goto(x, y)
    turtle.down()  # 开始绘制
    turtle.color("#04B45F")
    turtle.speed(0)

    # 循环
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)

    turtle.up()  # 结束绘制


def rectangles(depth, size, x, y):

    if depth == 0:
        return

    else:
        # 计算当前矩形的长和宽
        width = size / 2
        length = size
        one_rectangle(x, y, length, width)

        if depth == 1:
            return

        # 如果深度大于1，绘制两个较小的矩形
        else:
            # 计算新矩形的尺寸
            new_size = size / 2
            # 分别计算左边和右边矩形的起始坐标
            new_x_left = x - new_size
            new_y_left = y

            # 右边
            new_x_right = x + length
            new_y_right = y

            # 递归绘制左边的矩形
            rectangles(depth - 1, new_size, new_x_left, new_y_left)
            # 递归绘制右边的矩形
            rectangles(depth - 1, new_size, new_x_right, new_y_right)


def main():
    depth = int(input("Enter the depth："))
    size = int(input("Enter the size："))
    init(size)

    # 初始矩形的左下角坐标
    rectangles(depth, size, -size /100, -size / 4)

    turtle.done()


if __name__ == "__main__":
    main()
