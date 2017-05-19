age = 24
print('My age is '+str(age)+' years')
print('My age is {0} years'.format(age))

# Python 2 format. Currently not used.
print('My age is %d years' % age)
print('My age is %d %s %d %s ' % (age, 'years', 6, 'months'))

for i in range(1, 12):
    print('No. %2d squared is %4d and cubed is %4d' % (i, i**2, i**3))

print('Pi is %1.50f' % (22/7))

print('My age is {0} {1} {2} {3} '.format(age, 'years', 6, 'months'))


for i in range(1, 12):
    print('No. {0:2} squared is {1:4} and cubed is {2:4}'.format(i, i**2, i**3))

print('Pi is {0:1.50f}'.format(22/7))

for i in range(1, 12):
    print('No. {:2} squared is {:4} and cubed is {:4}'.format(i, i**2, i**3))