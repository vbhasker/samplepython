shopping_list = ['eggs', 'pasta', 'spam', 'milk', 'bread', 'rice']

for item in shopping_list:
    if item == 'spam':
        continue
    print('Buy {0}'.format(item))
