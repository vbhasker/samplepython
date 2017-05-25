fruits = {"apple": "I love this fruit",
          "lemon": "sour yellow fruit"}

print(fruits["apple"])

fruits["lime"] = "sour green fruit"

print(fruits)

# del fruits["lemon"]

print(fruits)

# dictionary can contain any type together but it needs to be immutable.
# can have tuple but not list.

# for i in range(10):
#     for snack in fruits:
#         print(fruits[snack])
#     print('-'*40)

for sort_keys in sorted(fruits.keys()):
    print('{} -> {}'.format(sort_keys, fruits[sort_keys]))

# view object by reference dict_keys

fruit_keys = fruits.keys()
print(fruit_keys)

fruits['peach'] = 'another fruit'
# even though the keys are not extracted after appending another value to dictionary, new values are printed
print(fruit_keys)
