from Player import *


p1 = Player(17,16)
print "get ready"
while(not is_pressed("esc")):
    p1.runSchem1()




GPIO.cleanup()
