"""
example 2
mkp
"""
MONTHS = ['January','February','March','April','May','June','July','August', 'September', 'October','November','December']



def main():
    date = input("Enter date in format XX/XX/XXXX: ")
    month = MONTHS[ int(date[0:2]) - 1]
    day = date[3:5]
    year = date[6:10]
    print(month, end='')  # May 24, 2020
    print(' ', end='')
    print(day, end='')
    print(', ', end='')
    print(year, end='')

main()

    
    
