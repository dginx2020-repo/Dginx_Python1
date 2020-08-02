# variable Declaration
'''
a = 10
b = 20
c = 'Deepti Ranjan Das'
list1 = [1, 2, 3, 10.5, 5, 5, 'Mango']
dict1 = {1: 56.2, 2: 'Orange'}
set1 = {1, 2, 10, 49, 50, 9.20}
set2 = {1, 3, 20, 20, 56}
tuples1 = ('Apple', 'Apple', 'apple', 30, 30, 49)
# print(list1)
print(set(tuples1))
'''
# Arithmetic Operation
num1 = int(input('Enter the 1st value:'))
num2 = int(input('Enter the 2nd Value:'))
set1 = {1: '+', 2: '-', 3: '*', 4: '/'}
print('Available Operation', set1)
opp = int(input('Enter your selection:'))

while opp in range(1, 5):
    if opp == 1:
        print('Addition of %d and %d is %d' % (num1, num2, num1 + num2))
        break
    elif opp == 2:
        print('Sub of %d and %d is %d' % (num1, num2, num1 - num2))
        break
    elif opp == 3:
        print('Multiply of %d and %d is %d' % (num1, num2, num1 * num2))
        break
    elif opp == 4:
        print('Div of %d and %d is %d' % (num1, num2, num1 / num2))
        break
    else:
        break
else:
    print('Invalid Selection')







