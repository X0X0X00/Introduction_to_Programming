"""
example 1 Wed
week 5
mkp
"""


def main():
    list = []
    x = 1
    # n! = n* (n-1)!
    list.append(x) # to keep 0!
    for i in range(1,101):
        x = x *i
        list.append(x)

    print(list)

main()
    
