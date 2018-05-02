from random import randint
from tqdm import tqdm

def r(x, y):
    return randint(x, y)

a = 0
b = 0
c = 0
global result
result = 0

loopt = 100000000  # How many simulations?

for ii in tqdm(range(loopt)):
    while True:
        n = r(0, 2)
        if n == 0:
            a += 1
        elif n == 1:
            b += 1
        else:
            c += 1

        if a != 0 and b != 0 and c != 0:
            #print("Get. a:%i b:%i c:%i" % (a, b, c))
            avg = a + b + c
            result += avg
            break

    a = 0
    b = 0
    c = 0

average = result / loopt
print("average: %f" % average)

