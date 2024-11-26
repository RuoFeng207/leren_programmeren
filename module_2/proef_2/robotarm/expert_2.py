from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.expert import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[2],0)
# your code starts here:
a=9
b=8
for z in range(9):
    robotArm.grab()
    robotArm.scan()
    coller = robotArm.scan()
    if coller =="red":
        for x in range(a):
            robotArm.moveRight()
        robotArm.drop()
        for y in range(b):
            robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveRight()
    a-=1
    b-=1


# your code ends here


# report the results of the mission
robotArm.report()

# want help? Unlock code below!
# robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

