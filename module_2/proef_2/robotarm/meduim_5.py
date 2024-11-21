from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.medium import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[5],0)
# your code starts here:
x=9

for a in range(5):
    robotArm.grab()
    for i in range(x):
        robotArm.moveRight()
        
    robotArm.drop()
    x-=1
    for i in range(x):
        robotArm.moveLeft()
    x-=1


# your code ends here


# report the results of the mission
robotArm.report()

# want help? Unlock code below!
# robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

