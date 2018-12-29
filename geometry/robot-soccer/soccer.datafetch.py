import ev3dev.ev3 as ev3
import time

left = ev3.LargeMotor('outB')
right = ev3.LargeMotor('outD')
color = ev3.ColorSensor()
dist = ev3.InfraredSensor()

color.mode = 'COL-COLOR'

# === [constants] === #

# Wall Constants
WALL_UL = 1
WALL_UR = 2
WALL_DL = 3
WALL_DR = 4

# Color Sensor Convert
RED = 5
YELLOW = 4
GREEN = 3
BLUE = 2

# Speed Constants
FAST_SPEED = 1000
MEDIUM_SPEED = 500
SLOW_SPEED = 200

# Speed of increment. Whenever robot is 'safe' to run.
SPEED_DELTA = 1.5

# Relative angle to the originla position, which should be facing to the enemy's goal.
worldAngle = 0

# Section size; where the robot will scan a bit, then turn its angle.
sectionSize = 500

# Angle that the robot will be turning at when the robot finished scanning a section.
turningAngle = 30

# Distance threshold that the robot will be stop at and record where the soccer is at.
DISTANCE_THRESHOLD = 40

# Sleep duration (seconds)
SLEEP_CONSTANT = 2.5

defaultMessage = '''
=== [Soccer Project] ===

# +  Calculations
# -  Test Case
# ->>>  DataFetcher  <<<
# +  Production

========================
'''

print(defaultMessage)

askMessage = '''

   int cases
     \|#|/
      \|/
       v

[[
    # -0  Calibrate: Rotation,
    # -1  Calibrate: Motor Distance
], [
    # -2  Test Case: Infrared Sensor,
    # -3  Test Case: Color Sensor
], [
    # -4  Interactive Terminal
]]

_case > '''


class AllMotor:
    @staticmethod
    def wait():
        left.wait_while('running')
        right.wait_while('running')

    @staticmethod
    def stop():
        left.stop(stop_action='hold')
        right.stop(stop_action='hold')


def fetch_rotation():
    print('# Begin: Calibrate: Rotation')
    loop = [-500, 500, -1000, 1000, -2000, 2000]
    Motor(loop=loop, forward=False)
    print('# Ended: Calibrate: Rotation')


def fetch_motor():
    print('# Begin: Calibrate: Motor Distance')
    loop = [500, 1000, 1500, 2000]
    Motor(loop=loop, forward=True)
    print('# Ended: Calibrate: Motor Distance')


class Motor:
    @staticmethod
    def forward(distance: int = 0):
        left.run_to_rel_pos(position_sp=distance, speed_sp=MEDIUM_SPEED, stop_action='hold')
        right.run_to_rel_pos(position_sp=distance, speed_sp=MEDIUM_SPEED, stop_action='hold')

    @staticmethod
    def custom(distance: int = 0):
        left.run_to_rel_pos(position_sp=distance, speed_sp=MEDIUM_SPEED, stop_action='hold')
        right.run_to_rel_pos(position_sp=-distance, speed_sp=MEDIUM_SPEED, stop_action='hold')
    
    def __init__(self, loop: list = [], forward: bool = False):
        print('Looping Motor. Total %s times, forward: %s' % (len(loop), forward))
        jj = 0
        for j in loop:
            jj += 1
            if forward:
                print('# c%s: position={ distance=%s }' % (jj, j))
                self.forward(distance=j)
            else:
                print('# c%s: position={ left=%s, right=%s }' % (jj, j, -j))
                self.custom(distance=j)
            AllMotor.wait()
            print('# c%s: done.' % jj)
            if len(loop) != jj:
                time.sleep(SLEEP_CONSTANT)


def tc_infsensor():
    print('# Start: Test Case: Infrared Sensor')
    recent_history = []
    loop_count = 0
    while True:
        try:
            sensor_data = int(dist.value())
            recent_history.append(sensor_data)
            if len(recent_history) >= 10:
                print('# c%i | Distance: [%i, %i, %i, %i, %i, %i, %i, %i, %i, %i]' % (
                    loop_count, recent_history[0], recent_history[1], recent_history[2], recent_history[3],
                    recent_history[4], recent_history[5], recent_history[6], recent_history[7], recent_history[8],
                    recent_history[9])
                    )
                recent_history = []
                loop_count = 0
            else:
                pass
        except (KeyboardInterrupt, SystemExit):
            break
        pass

    print('# Ended: Test Case: Infrared Sensor')


def tc_colorsensor():
    print('# Start: Test Case: Color Sensor')
    while True:
        try:
            print('Current Color: r%s g%s b%s' % (color.value(0), color.value(1), color.value(2)))
        except (KeyboardInterrupt, SystemExit):
            break
        pass
    print('# Ended: Test Case: Color Sensor')


def interactive():
    shell = input('shell > ')
    if shell == 'exit' or len(shell) == 0:
        return True
    eval(shell)
    interactive()

class ColorHelper:
    @staticmethod
    def is_ball(r, g, b):
        total = r + g + b
        r_percentage = r / total
        # g_percentage = g / total # Not used yet...
        b_percentage = b / total
        if g > r > b:
            print('[Color] Current: is_ball | TRUE | CON1 | %s, %s, %s' % (r, g, b))
            return True
        elif r_percentage > 0.35 and b_percentage < 0.05:
            print('[Color] Current: is_ball | TRUE | CON2 | %s, %s, %s' % (r, g, b))
            return True
        else:
            print('[Color] Current: is_ball | FALSE | %s, %s, %s' % (r, g, b))
            return False

    def is_wall(self, r, g, b):
        if self.get_color_of_wall(r, g, b) is not False and self.is_ball(r, g, b) is not True:
            return True
        else:
            return False

    @staticmethod
    def get_color_of_wall(r, g, b):
        # Up Left; Red (255, 0, 0).
        if r > g and r > b:
            print('[Color] Current: is_wall | UP-LEFT | r%s, g%s, b%s' % (r, g, b))
            return WALL_UL
        # Up Right; Yellow (255, 255, 0).
        elif MathHelper(r, g, 100) and (r + g) > b:
            print('[Color] Current: is_wall | UP-RIGHT | r%s, g%s, b%s' % (r, g, b))
            return WALL_UR
        # Down Left; Blue (0, 0, 255).
        elif b > r and b > g:
            print('[Color] Current: is_wall | DOWN-LEFT | r%s, g%s, b%s' % (r, g, b))
            return WALL_DL
        # Down Right; Green (0, 255, 0).
        elif g > r and g > b:
            print('[Color] Current: is_wall | DOWN-RIGHT | r%s, g%s, b%s' % (r, g, b))
            return WALL_DR
        else:
            print('[Color] Current: is_wall | NOT-WALL | r%s, g%s, b%s' % (r, g, b))
            return False


class SensorHelper:
    def distance(threshold: int = 30):
        while True:
            val = dist.value()
            if val < threshold:
                return True
    
    def color_get_sample(sample: int = 100):
        r = 0
        g = 0
        b = 0
        
        for i in range(sample):
            r += color.value(0)
            g += color.value(1)
            b += color.value(2)
        
        return r, g, b


def colorclass():
    samples = SensorHelper.color_get_sample()

    if ColorHelper.is_ball(r=samples[0], g=samples[1], b=samples[2]):
        print('[Color] Current: is_ball | %s, %s, %s' % (samples[0], samples[1], samples[2]))
    elif ColorHelper.is_wall(r=samples[0], g=samples[1], b=samples[2]):
        print('[Color] Current: is_wall | %s, %s, %s' % (samples[0], samples[1], samples[2]))
    else:
        return False

def ask():
    digit = int(input(askMessage))
    
    if digit == 0:
        fetch_rotation()
    elif digit == 1:
        fetch_motor()
    elif digit == 2:
        tc_infsensor()
    elif digit == 3:
        tc_colorsensor()
    elif digit == 4:
        interactive()
    elif digit == 5:
        colorclass()
    else:
        raise ValueError('Invalid input: %s' % digit)
    ask()

ask()
