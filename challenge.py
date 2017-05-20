name = input('Please enter your name: ')
age = int(input('What is your age, {0}? '.format(name)))

# if (age >= 18) and (age < 31):
if 18 <= age < 31:
    print('Welcome to the holiday!')
else:
    print('Sorry, this holiday is only for people under 31 and above 18 years old')
