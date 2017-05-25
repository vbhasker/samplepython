shopping_list = ['eggs', 'pasta', 'spam', 'milk', 'bread', 'rice']

for item in shopping_list:
    if item == 'spam':
        continue
    print('Buy {0}'.format(item))

# while loop example for break
available_exits = ['north', 'south_east']
chosen_exit = ''
while chosen_exit not in available_exits:
    chosen_exit = input('Enter the exit direction: ')
    if chosen_exit == 'quit':
        print('Game over!')
        break

# this else is for the while. If the statement becomes true to exit the loop this gets executed.
# doesn't get executed when break.
else:
    print("successfully exited!")


even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
ordered_numbers = sorted(numbers)

if sorted(numbers) == ordered_numbers:
    print('They are the same list contents')
