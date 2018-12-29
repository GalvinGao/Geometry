import ev3dev.ev3 as ev3
import logging
import random
import _thread


# === [initiation] === #
logging.basicConfig(level=logging.INFO, format='%(asctime)s $ %(name)s $ %(thread)d | [%(levelname)s]: %(message)s ')
logger = logging.getLogger(__name__)

# ev3 Classes Initiation
left = ev3.LargeMotor('outB')
right = ev3.LargeMotor('outD')
kicker = ev3.MediumMotor('outA')
color = ev3.ColorSensor()
dist = ev3.InfraredSensor()

# Change color sensor mode to COL-COLOR (Outputs RGB)
color.mode = 'RGB-RAW'


# === [configuration] === #

# Wall Constants
WALL_UL = 1
WALL_UR = 2
WALL_DL = 3
WALL_DR = 4

# Speed Constants
FAST_SPEED = -1000
MEDIUM_SPEED = -500
SLOW_SPEED = -200

# Speed of increment. Whenever robot is 'safe' to run. (not used yet)
SPEED_DELTA = 1.5

# Relative angle to the original position, which should be facing to the enemy's goal.
worldAngle = 0

## Plan B (Self-plan; semi intelligence)

# Section size; where the robot will scan a bit, then turn its angle.
sectionSize = 500

# Angle that the robot will be turning at when the robot finished scanning a section.
turningAngle = 30

# Distance threshold that the robot will be stop at and record where the soccer is at.
DISTANCE_THRESHOLD = 40


# === [classes] === #

class Rotation:
    def apply(self, angle: int = 0):
        left_distance = angle * 5.56
        right_distance = -left_distance
        left.run_to_rel_pos(position_sp=left_distance, speed_sp=self.speed, stop_action='hold')
        right.run_to_rel_pos(position_sp=right_distance, speed_sp=self.speed, stop_action='hold')
        if self.wait:
            AllMotor.wait()
    '''
    def with_ball(angle: int = 0):
        if angle < 0:
            left.run_to_rel_pos(position_sp=)
    '''

    def __init__(self, speed: int = FAST_SPEED, wait: bool = False):
        self.speed = speed
        self.wait = wait

# To move a robot forward, do this
# section=Movement(speed=FAST_SPEED)
# section.forward(distance=300)
# 
# To custom movement, do this
# section=Movement(speed=SLOW_SPEED)
# section.special(left=100, right=200)


class Movement:
    def __init__(self, speed: int = FAST_SPEED, wait: bool = False, wait_left: bool = False, wait_right: bool = False):
        """
        :param speed: int
        :param wait: bool
        :param wait_left: bool
        :param wait_right: bool
        """
        self.speed = speed
        self.wait = wait
        self.wait_left = wait_left
        self.wait_right = wait_right

    def special(self, left_motor: int = 0, right_motor: int = 0):
        left.run_to_rel_pos(position_sp=left_motor, speed_sp=self.speed, stop_action='hold')
        right.run_to_rel_pos(position_sp=right_motor, speed_sp=self.speed, stop_action='hold')
        self.will_wait()

    def forward(self, distance: int = 0):
        left.run_to_rel_pos(position_sp=distance, speed_sp=self.speed, stop_action='hold')
        right.run_to_rel_pos(position_sp=distance, speed_sp=self.speed, stop_action='hold')
        self.will_wait()

    def will_wait(self):
        if self.wait:
            if self.wait_left or self.wait_right:
                if self.wait_left:
                    left.wait_while('running')
                elif self.wait_right:
                    right.wait_while('running')
                else:
                    AllMotor.wait()
            else:
                AllMotor.wait()


class AllMotor:
    @staticmethod
    def wait():
        left.wait_while('running')
        right.wait_while('running')

    @staticmethod
    def stop():
        left.stop(stop_action='hold')
        right.stop(stop_action='hold')
    
    @staticmethod
    def run(speed: int = FAST_SPEED):
        left.run_forever(speed_sp=speed)
        right.run_forever(speed_sp=speed)


class LogHelper:
    @staticmethod
    def new_thread(thread_name: str = '', thread_id: int = 0):
        logger.info('[Thread] Thread [%s] has been started with id [%s]' % (thread_name, thread_id))


class UnitConverter:
    @staticmethod
    def distance(actual: int = 0):
        return 500 * actual
    
    @staticmethod
    def angle(actual: int = 0):
        return 11.11 * actual


class MathHelper:
    @staticmethod
    def about(source: int = 0, compare_to: int = 0, accuracy: int = 0):
        if abs(source - compare_to) <= accuracy:
            return True
        else:
            return False


class SensorHelper:
    @staticmethod
    def distance(threshold: int = 30):
        while True:
            val = dist.value()
            if val < threshold:
                return True

    @staticmethod
    def color_get_sample(sample: int = 100):
        r = 0
        g = 0
        b = 0
        
        for i in range(sample):
            r += color.value(0)
            g += color.value(1)
            b += color.value(2)
        
        return r, g, b


class ColorHelper:
    @staticmethod
    def is_ball(r, g, b):
        total = r + g + b
        r_percentage = r / total
        # g_percentage = g / total # Not used yet...
        b_percentage = b / total
        if g > r > b:
            return True
        elif r_percentage > 0.35 and b_percentage < 0.05:
            return True
        else:
            return False

    @staticmethod
    def is_wall(self, r, g, b):
        if self.get_color_of_wall(r, g, b) is not False and self.is_ball(r, g, b) is not True:
            return True
        else:
            return False

    @staticmethod
    def get_color_of_wall(r, g, b):
        # Up Left; Red (255, 0, 0).
        if r > g and r > b:
            return WALL_UL
        # Up Right; Yellow (255, 255, 0).
        elif MathHelper(r, g, 100) and (r + g) > b:
            return WALL_UR
        # Down Left; Blue (0, 0, 255).
        elif b > r and b > g:
            return WALL_DL
        # Down Right; Green (0, 255, 0).
        elif g > r and g > b:
            return WALL_DR
        else:
            return False


def find_object_occurrence():
    try:
        rotate = Rotation(speed=MEDIUM_SPEED, wait=True)
        one_section = Movement(speed=FAST_SPEED, wait=True)
        rotate.apply(angle=-30)
        one_section.forward(distance=sectionSize)
    except:
        logger.exception('Unexpected exception raised in function find_object_occurrence. See details below.', exc_info=True)


def distance_watcher():
    while True:
        val = ev3.InfraredSensor().value()
        if val < DISTANCE_THRESHOLD:
            AllMotor.stop()
            break


class PlanA():
    def __init__(self):
        thread_id = _thread.start_new_thread(self.apply, ())
        LogHelper.new_thread(thread_name='plan_a.threading', thread_id=thread_id)

    @staticmethod
    def apply():
        left.run_timed(time_sp=2450, speed_sp=FAST_SPEED, stop_action='hold')
        AllMotor.wait()
        left.run_timed(time_sp=1500, speed_sp=FAST_SPEED, stop_action='hold')
        right.run_timed(time_sp=1500, speed_sp=FAST_SPEED, stop_action='hold')
        AllMotor.wait()
        left.run_to_rel_pos(position_sp=40, speed_sp=MEDIUM_SPEED, stop_action='hold')
        right.run_to_rel_pos(position_sp=400, speed_sp=MEDIUM_SPEED, stop_action='hold')
        AllMotor.wait()
        left.run_timed(time_sp=3500, speed_sp=FAST_SPEED, stop_action='hold')
        right.run_timed(time_sp=3500, speed_sp=FAST_SPEED, stop_action='hold')
        AllMotor.wait()
        AllMotor.stop()


class PlanB:
    def __init__(self):
        try:
            # Fire distance_watcher() that will loop around the Infrared Sensor to monitor the distance. (Monitoring sensor)
            distance_watcher_thread = _thread.start_new_thread(distance_watcher, ())
            LogHelper.new_thread(thread_name='distance_watcher', thread_id=distance_watcher_thread)

            # Fire find_object_occurrence() to traverse the field to find the object. (Motor moving)
            find_ball_thread = _thread.start_new_thread(find_object_occurrence, ())
            LogHelper.new_thread(thread_name='find_object_occurrence', thread_id=find_ball_thread)

        except (KeyboardInterrupt, SystemExit):
            raise KeyboardInterrupt('Shutting down...')

        except Exception:
            logger.exception('Unexpected error occurred when trying to fire a thread. Details were at below.', exc_info=True)

    @staticmethod
    def apply():
        AllMotor.run()

        while True:
            if SensorHelper.distance(threshold=5) is True:
                break
        
        AllMotor.stop()

        samples = SensorHelper.color_get_sample()

        if ColorHelper.is_ball(r=samples[0], g=samples[1], b=samples[2]):
            pass
        else:
            return False
        
        move = Movement(wait=True)
        move.forward(distance=-500)
        
        rotate = Rotation()
        rotate.apply(angle=180)
        
        move.forward(distance=-500)
        
        kicker.run_to_rel_pos(position_sp=2000, speed_sp=FAST_SPEED, stop_action='hold')
        kicker.wait_while('running')
        
        rotate.apply(angle=-135)
        
        AllMotor.run()
        
        while True:
            if SensorHelper.distance(threshold=10) is True:
                break
        
        samples = SensorHelper.color_get_sample()
        
        if ColorHelper.is_ball(r=samples[0], g=samples[1], b=samples[2]):
            AllMotor.run(speed=1000)
        elif ColorHelper.is_wall(r=samples[0], g=samples[1], b=samples[2]):
            rotate.apply(angle=random.randint(0,360))
        else:
            return False
        
        #AllMotor.stop()
        

class PlanC:
    @staticmethod
    def apply():
        AllMotor.run(speed=FAST_SPEED)
        
        while True:
            if SensorHelper.distance(threshold=10) is True:
                rotate = Rotation(wait=True)
                rotate.apply(angle=random.randint(0,720)-360)
                return False

def shell():
    code = input('shell_> ')
    eval(code)
    shell()

def run():
    while True:
        PlanB.apply()

run()
