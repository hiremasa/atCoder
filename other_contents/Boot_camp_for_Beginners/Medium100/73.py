a, b, c = map(int, input().split())
from decimal import *
a = Decimal(a) ** Decimal('0.5')
b = Decimal(b) ** Decimal('0.5')
c = Decimal(c) ** Decimal('0.5')

if a+b-c < 0:
    print("Yes")
else:
    print("No")
