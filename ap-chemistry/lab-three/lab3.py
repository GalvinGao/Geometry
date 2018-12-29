import math
from decimal import *

a0 = Decimal('5.29177') * Decimal('10') ** Decimal('-11')
rmax = Decimal('10') * a0
areas = 100

getcontext().prec = 1000

sumValue = Decimal('0')

for n in range(areas):
	tempR = Decimal(n) * Decimal(rmax) / areas
	psi = Decimal('2.0') / Decimal(Decimal(a0) ** Decimal('1.5')) * Decimal(math.exp(-tempR / a0))
	tempR = n * rmax / Decimal(areas)
	tempA = Decimal(psi) ** Decimal('2') * tempR ** Decimal('2') * rmax / Decimal(areas)
	sumValue = sumValue + tempR * tempA
print(sumValue)
