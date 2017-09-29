# Regular expressions

import re

ingredient = 'Kumquat: 2 cups'
print(ingredient)

pattern_text = r'(?P<ingredient>\w+):\s+' \
               r'(?P<amount>\d+)\s+' \
               r'(?P<unit>\w+)'

pattern = re.compile(pattern_text)

match = pattern.match(ingredient)
print(match is None)
print(match.groups())
print(match.group('amount'))

ingredient_pattern = re.compile(
    r'(?P<ingredient>\w+):\s+'  # better way to represent the regular expression
    r'(?P<amount>\d+)\s+'
    r'(?P<units>\w+)'
)
match_new = ingredient_pattern.match(ingredient)
print(match_new is None)
print(match_new.groups())
print(match_new.group('units'))


# Formatting strings

code = 'IAD'
location = 'Dulles Intl Airport'
max_temp = 32
min_temp = 13
precipitation = 0.4

print('{code:3s} : {location:19s} : {max_temp:3d} / {min_temp:3d} / {precipitation:5.2f}'
      .format(code=code, location=location,
              max_temp=max_temp, min_temp=min_temp,
              precipitation=precipitation))

# vars stores all the variables as a dictionary

print(vars())

print('{code:3s} : {location:19s} : {max_temp:3d} / {min_temp:3d} / {precipitation:5.2f}'
      .format_map(vars()))

print('%3s : %19s : %3d / %3d / %5.2f' % (code, location, max_temp, min_temp, precipitation))

print('{0:3s} : {1:19s} : {2:3d} / {3:3d} / {4:5.2f}'.format(code, location, max_temp, min_temp, precipitation))

