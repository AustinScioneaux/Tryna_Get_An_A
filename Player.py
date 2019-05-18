from Robot import *
from Controls import *

class Player(object):

    def __init__(self, leftW, rightW):
        self.leftW = leftW
        self.rightW = rightW
        self.robot= Robot(self.leftW, self.rightW)
        self.controls = Controls()

    #There are two control schematic options. These two function should NEVER both be called in the same program
        
    def runSchem1(self):
        if(self.robot.pinsRaised == False):
            raise Exception('Pins were not initialized for this robot')
        #elif prevents problems from both forward and backward being pressed
        if (is_pressed(self.controls.forward)):
            self.robot.forward()
            
        elif (is_pressed(self.controls.backward)):
            self.robot.backward()
            

        #allow simultaneos left and right turn
        if(is_pressed(self.controls.leftTurn)):
            self.robot.turnL()

        if(is_pressed(self.controls.rightTurn)):
            self.robot.turnR()
    
        
        if( (not is_pressed(self.controls.forward)) and (not is_pressed(self.controls.backward)) and (not is_pressed(self.controls.leftTurn) ) and (not is_pressed(self.controls.rightTurn)) ):
            #if nothing is pressed stop both wheels
            self.robot.stop()
        elif( (not is_pressed(self.controls.forward)) and (not is_pressed(self.controls.backward)) and (not is_pressed(self.controls.leftTurn) ) and (is_pressed(self.controls.rightTurn))):
            #if everything is NOT pressed EXCEPT for rightTurn
            self.robot.stopR()
        elif( (not is_pressed(self.controls.forward)) and (not is_pressed(self.controls.backward)) and (is_pressed(self.controls.leftTurn) ) and (not is_pressed(self.controls.rightTurn))):
            #if everything is NOT pressed EXCEPT for leftTurn
            self.robot.stopL()

    def runSchem2(self):
        #program only allows for 1 command for the left wheel
        if(is_pressed(self.controls.lf)):
            self.robot.leftForward()
        elif(is_pressed(self.controls.lb)):
            self.robot.leftBackw()
        else:
            self.robot.stopL()

        #program only allows for 1 command for the right wheel
        if(is_pressed(self.controls.rf)):
            self.robot.rightForward()
        elif(is_pressed(self.controls.rb)):
            self.robot.rightBackw()
        else:
            self.robot.stopR()
