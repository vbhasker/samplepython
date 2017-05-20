for i in range(1, 12):
    print('No {} squared is {} and cubed is {:4}'.format(i, i**2, i**3))

# name = input("What is your name:")
# age = int(input("how old are you, {0}?".format(name)))
name = 'test'
age = 16
print(age)

if age >= 18:
    print('You are old enough to vote.')
else:
    print('{0}, Please come back after {1} years!'.format(name, 18-age))

if (age < 16) or (age >= 65):
    print('Enjoy your free time')
else:
    print('Have a good day at work!')


empty = ''
if empty:
    print('empty is true')
else:
    print('empty is false')

no_value = None
if no_value:
    print('None is true')
else:
    print('None is false')

