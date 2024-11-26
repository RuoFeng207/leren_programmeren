from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.expert import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[4],0)
# your code starts here:
a=7
b=8
c=9
for x in range(7):
    chek = robotArm.stackEmpty()
    if chek== True:
        pass
    else:
        robotArm.grab()
        coller = robotArm.scan()
        if coller =="red":
            for red in range(a):
                robotArm.moveRight()
            robotArm.drop()
            a-=1
            b-=1
            c-=1
        
            for red in range(a):
                robotArm.moveLeft()
        elif coller =="green":
            for red in range(b):
                robotArm.moveRight()
            robotArm.drop()
            a-=1
            b-=1
            c-=1
        
            for red in range(b):
                robotArm.moveLeft()
        else:
            for green in range(c):
                robotArm.moveRight()
            robotArm.drop()
            a-=1
            b-=1
            c-=1
        
            for red in range(c):
                robotArm.moveLeft()
        
        
        

        
# your code ends here


# report the results of the mission
robotArm.report()

# want help? Unlock code below!
# robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

