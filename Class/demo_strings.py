"""
strings demo

mkp
"""
x = 'HeElo world!'

for loop_variable in x:
    print(loop_variable, end='')

print('\n***************************')
length = len(x)

for i in range(length):
    print(i,' ', x[i])


# How to get error. Try:

for i in x:
    print(x[i], end='')
    



    
