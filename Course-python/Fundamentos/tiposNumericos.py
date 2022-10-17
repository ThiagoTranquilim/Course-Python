#Inteito
print(dir(int))

#Float
print(dir(float))

from decimal import Decimal, getcontext
print(dir(Decimal))
print(Decimal(1)/Decimal(7))

getcontext().prec = 4
print(Decimal(1)/Decimal(7))
