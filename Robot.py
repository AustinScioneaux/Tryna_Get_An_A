import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)

#Robot is outfitted with two methods of movement. One where player controls individual wheels at a time
# and another where there is a dual wheel forwards and dual wheel backwards
# with a left and right turn future.
class Robot(object):
    cw = 6
    ccw = 7.5

    def __init__(self, leftW, rightW):

        self.leftW = leftW
        self.rightW = rightW

        #setup pins
        GPIO.setup(leftW, GPIO.OUT)
        GPIO.setup(rightW, GPIO.OUT)
        #declare some pwm object for each wheel
        self.l = GPIO.PWM(leftW, 50)
        self.r = GPIO.PWM(rightW, 50)

        #start em at 0 workload
        self.l.start(0)
        self.r.start(0)

    def leftForw(self):
        #need ccw for left to move forward
        self.l.ChangeDutyCycle(self.cw)

    def leftBackw(self):
        #need cw for left to move backward
        self.l.ChangeDutyCycle(self.cw)

    def rightForw(self):
        #need cw for right to move forward
        self.r.ChangeDutyCycle(self.ccw)

    def rightBackw(self):
        #neede ccw for right to move backward
        self.r.ChangeDutyCycle(self.ccw)
        
    def forward(self):
        #ccw for left cw for right
        self.l.ChangeDutyCycle(self.ccw)
        self.r.ChangeDutyCycle(self.cw)

    def backward(self):
        #ccw for right cw for left
        self.l.ChangeDutyCycle(self.cw)
        self.r.ChangeDutyCycle(self.ccw)

    def turnL(self):
        self.rightForw()

    def turnR(self):
        self.leftForw()

    def stopL(self):
        self.l.ChangeDutyCycle(0)

    def stopR(self):
        self.r.ChangeDutyCycle(0)

    def stop(self):
        #stop all wheels
        self.l.ChangeDutyCycle(0)
        self.r.ChangeDutyCycle(0)
        


    
