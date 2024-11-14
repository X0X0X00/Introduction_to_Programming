"""
mkp
week 3, ex 1

"""

def main():
     x = eval(input("Enter number x: "))
     for n in range(5):
          x = 3.9 * x * (x-1)
          print(x)

main()
