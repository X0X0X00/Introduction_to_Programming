"""
mkp
Week 3 ex 2
"""


def main():
     intrest = eval(input('Intrest: '))
     money = int(input("Initial capital: "))
     for year in range(10):
          money = money + intrest*money
          print(money)

main()
          
