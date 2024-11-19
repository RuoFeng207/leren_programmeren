from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.beginner import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[2],0)
# your code starts here:
for x in range(6):
    robotArm.moveRight()
    robotArm.grab()
    coller = robotArm.scan()
    if coller=="blue":
        robotArm.moveLeft()
        robotArm.drop()
    else:
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
        robotArm.moveLeft()

    
# your code ends here


# report the results of the mission
robotArm.report()

# want help? Unlock code below!
# robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

