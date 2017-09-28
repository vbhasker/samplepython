from sys import maxsize
from math import factorial
from math import sqrt
from math import log
from decimal import Decimal
from decimal import ROUND_DOWN # default is round even

print(factorial(52))

print(log(maxsize, 2))

print('id of the number 2: ', id(103232))

# decimal from string and avoid decimal from float comparision
penny = Decimal('0.01')

tax_rate = Decimal('8.25')/Decimal(100)
purchase_amount = Decimal('12.95')
final_price = Decimal(purchase_amount*tax_rate) + purchase_amount
print('final decimal price', final_price)

tax_rate = 8.25/100
purchase_amount = 12.95
float_final_price = purchase_amount*tax_rate + purchase_amount
print('final float price', float_final_price)

final_price = final_price.quantize(penny, ROUND_DOWN)
print(final_price)

tax_rate = Decimal(8.25)/Decimal(100)
purchase_amount = Decimal(12.95)
final_price = Decimal(purchase_amount*tax_rate) + purchase_amount
print(final_price)

print(sqrt(2)*sqrt(2))
