"""
mkp
"""

def sum():
    sum = 0
    user_input = input('enter number or press ENTER when you are done')
    while True: #user_input != "":
        if user_input == "":
            break
        sum = sum + float(user_input)
        user_input = input('enter number or press ENTER when you are done')
    print(sum)

if __name__=='__main__':
    sum()
