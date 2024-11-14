"""
mkp
week 3 ex 3
"""


def main():
     total = 0
     for student in range(200):
          grade =  eval(input('Enter grade for current student: '))
          total = total + grade
     print(total/200)

main()
