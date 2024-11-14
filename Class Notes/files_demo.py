"""
mkp
week 5
files demo
"""

def main():
    print('We print all lines')
    fd = open('fruits.txt', 'r')
    for line in fd:
        print(line, end='')
    fd.close()
    print('\nWe print 5 lines only')   
    fd = open('fruits.txt', 'r') 
    for i in range(5):
        line = fd.readline()
        print(line, end='')
    fd.close()
    print('\nWe print all lines again')   
    fd = open('fruits.txt', 'r')
    print(fd.read())
    fd.close()

    print('\nWe print all lines again again')   
    fd = open('fruits.txt', 'r')
    print(fd.readlines())
    fd.close()
    
        
main()
