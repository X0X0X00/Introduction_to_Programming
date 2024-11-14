"""
Sudocode
For successive years 1 through 10 
    Calculate principal = principal * (1 + apr) 
    Draw a bar for this year having a height corresponding to principal 
Wait for user to press Enter .
"""


# this code from week 3

def main():
     intrest = eval(input('Intrest as 0.1 for 10%: '))
     money = int(input("Initial capital: "))
     for year in range(10):
          money = money + intrest*money
          print(money)

main()
