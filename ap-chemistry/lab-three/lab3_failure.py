import math
from decimal import Decimal

a0 = 5.29177 * 10 ** (-11)
rmax = 10 * a0
areas = 100

sumValue=0

for n in range(areas):
	tempR=n*rmax/areas
	psi=2.0/(a0**(1.5))*math.exp(-tempR/a0)
	tempR=n*rmax/areas
	tempA=psi**2*tempR**2*rmax/areas
	sumValue=sumValue+tempR*tempA
print(sumValue)

