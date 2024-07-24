"""
mkp

"""


def happy():
    print('Happy birthday to you!')


def sing(person):
    happy()
    happy()
    print('Happy birthday dear, ', person + '!')
    happy()

def main():
    name = input('Name: ')
    sing(name)

main()

