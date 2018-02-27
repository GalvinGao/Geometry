#!/bin/usr/env python
#-*- coding: utf-8 -*-

# === Import required libraries === #
import math

# === Constants === #
GravC = 6.67 / math.pow(10, 11) # Gravitational Constant
massEarth = 6 * math.pow(10, 24) # Mass of the Earth
massMoon = 7 * math.pow(10, 24) # Mass of the Moon
earthRadius = 6 * math.pow(10, 3) # Radius of the Earth
moonRadius = 2 * math.pow(10, 3) # Radius of the Moon
velocityX = null # Velocity of X
velocityY = null # Velocity of Y
accX = null # Acceleration of X
accY = null # Acceleration of Y
timeConstant = 0.1 # Time Constant
loopTime = 1e7 # How many times we loop it

# == First Line of Calculation == #

serieX = 0 # AKA [xe]
serieY = 0 # AKA [ye]

# === Calculation === #

    # XE = Final Result serie {X}
    # Temp Actual Code
            # xTemp = xTemp + velocityX * timeConstant + 0.5 * accX * math.pow(timeConstant, 2)
            # yTemp = yTemp + velocityY * timeConstant + 0.5 * accY * math.pow(timeConstant, 2)

velocityX = velocityX + serieX * timeConstant

velocityY = velocityY + serieY * timeConstant

accX = xHelper * GravC * massMoon / math.pow(math.pow(x, 2) + math.pow(y, 2), 2 / 3)

accY = yHelper * GravC * massMoon / math.pow(math.pow(x, 2) + math.pow(y, 2), 2 / 3)

xHelper = xHelper + velocityX * timeConstant + 0.5 * accX * math.pow(timeConstant, 2)

yHelper = yHelper + velocityY * timeConstant + 0.5 * accY * math.pow(timeConstant, 2)

xTemp = - (xTemp + (velocityX + accX * timeConstant) * timeConstant + 0.5 * (xHelper + velocityX * timeConstant + 0.5 * accX * math.pow(timeConstant, 2) * GravC * massMoon / math.pow(math.pow(xHelper + velocityX * timeConstant + 0.5 * accX * math.pow(timeConstant, 2), 2) + math.pow(yHelper + velocityY * timeConstant + 0.5 * accY * math.pow(timeConstant, 2), 2), 2 / 3)) * math.pow(timeConstant, 2))

yTemp = - (yTemp + (velocityY + accY * timeConstant) * timeConstant + 0.5 * (yHelper + velocityY * timeConstant + 0.5 * accY * math.pow(timeConstant, 2) * GravC * massMoon / math.pow(math.pow(xHelper + velocityX * timeConstant + 0.5 * accX * math.pow(timeConstant, 2), 2) + math.pow(yHelper + velocityY * timeConstant + 0.5 * accY * math.pow(timeConstant, 2), 2), 2 / 3)) * math.pow(timeConstant, 2))

############################# Code Draft

# CALCULATIONS # NOTHING AT HERE I WONT LIE TO U PLEASE TRUST ME LOLLLLLLL. #
'''
math.pow(number, power) | math.pow(2,3) => 8  #平方 [Power]
y
xe = last xe+ Vx*T+1/2*ax*t^2
vx=last vx + last AX * Time
ax= x*G*Mm/(x^2+y^2)^2/3
xHelper(x)=xHelper+vx*Time+1/2*ax*Time^2
Y=last y+last vy*Time+1/2*last ay*Time^2

xe = last xe + (last vx + last AX * Time) * Time + 1/2* ((last x+last vx*Time+1/2*last ax*Time^2)*G*Mm/((last x+last vx*Time+1/2*last ax*Time^2)^2+(last y+last vy*Time+1/2*last ay*Time^2)^2)^2/3) * Time^2
'''

velocityY = 2 * math.pow(10, 3)
velocityX = 0
yHelper = 0
xHelper = 4 * math.pow(10, 5)
accX = 29.18125
accy = 0
xTemp = 9000
yTemp = 0

realTime = 0 # Equalivent effect as [Time (s)] in Excel. (此变量为自增变量，在运行单次 loopTime 周期时累加 timeConstant )

# === Graph the Data === #


import plotly.plotly as py
import plotly.graph_objs as go

plotX = []
plotY = []

# Use Constant first at here

for i in range(loopTime):
    # Loop the data here
        # formula here


    # Necessary updates to variables
    realTime += timeConstant
    plotX.append(xTemp)
    plotY.append(yTemp)

trace = go.Scatter(
    x = plotX,
    y = plotY
)

data = [trace]

py.iplot(data, filename='basic-line')
