#-*- coding: utf-8 -*-

'''
To install dependencies, use
$ pip install -r requirements.txt --user
'''

# === Print out Initialize text === #

initialMsg = '''
-============================-
| 10th Grade Winter Homework |
|   by Galvin G & Arthur M   |
|    Required Python 3.6+    |
|----------------------------|
|                            |
|       Initializing...      |
|                            |
-============================-

'''

print(initialMsg)

# === Import required libraries === #
import math
import matplotlib.pyplot as plt
from tqdm import tqdm

def poi(num, power):
    return math.pow(num, power)

def sqr(num):
    return math.pow(num, 2)

# === Global Variables === #
M = 6e24
G = 6.7e-11
p = 1.2
Re = 6e3
dt = 0.1
MM = 7e22
time = 0
loopTime = 1000000
xResult = []
yResult = []

# === First Line Variable Set === #
x = 400000
y = 0
vx = 0
vy = 2000
ax = - (x * G * MM) / poi(sqr(x)+sqr(y), (3/2))
ay = - (y * G * MM) / poi(sqr(x)+sqr(y), (3/2))
xe = 3 / 2 * Re
ye = 0
time += dt # Actual Time

calcMsg = '''
| - Processing Data...
'''

print(calcMsg)

# === Debug: Time Started === #
start = timeit.default_timer()

pbar = tqdm(range(loopTime))

# === Calculation === #
for i in pbar:
    x = x + vx * dt + 0.5 * ax * sqr(dt)
    y = y + vy * dt + 0.5 * ay * sqr(dt)
    vx = vx + ax * dt
    vy = vy + ay * dt
    ax = - (x * G * MM) / poi(sqr(x)+sqr(y), (3/2))
    ay = - (y * G * MM) / poi(sqr(x)+sqr(y), (3/2))
    xe = xe + vx * dt + 0.5 * ax * sqr(dt)
    ye = ye + vy * dt + 0.5 * ay * sqr(dt)

    xResult.append(xe)
    yResult.append(ye)

    # Update time
    time += dt

# === Debug: Time Ended === #
stop = timeit.default_timer()

print('| - Operation finished in', stop - start, 'ms')
print('| - Plotting image...')

plt.plot(xResult, yResult)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

finishMsg = '''
| - Done.
'''
print(finishMsg)
