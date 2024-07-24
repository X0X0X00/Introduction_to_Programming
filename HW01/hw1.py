# Zhenhao Zhang 2023/9/11

"""
    File: hw1.py
    Homework 1 assignemnt
    Zhenhao Zhang
"""

from turtle import *

def main():
    print("This program drawes a snowflake")
    color("blue")
    n = int(input("How many arms to draw? "))
    for i in range(n):
        # speed(1)
        forward(100)
        backward(100)
        left(360 / n)
    done()


main()
