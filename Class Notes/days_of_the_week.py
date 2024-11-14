"""
mkp
week5
Example 3
"""

WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
        'Sunday']

def main():
    day_number = int(input('Type number for 1 to 7 to display\
corresponding day of the week: '))
    print(WEEK[day_number-1])

main()
