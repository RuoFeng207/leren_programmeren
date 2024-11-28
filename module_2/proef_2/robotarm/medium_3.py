from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.medium import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[3],0)
# your code starts here:
a=0
for x in range(8):
    robotArm.moveRight()
for x in range(9):    
    robotArm.grab()
    coller=robotArm.scan()
    if coller=="white":
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
    else:
        robotArm.drop()
    if a<8:
        robotArm.moveLeft()
    a+=1
# for x in range(6):
#     robotArm.grab()
#     coller=robotArm.scan()
#     if coller =="white":
#         robotArm.moveRight()
#         robotArm.drop()
#         robotArm.moveRight()
#     else:
#         robotArm.drop()
#         robotArm.moveRight()
# your code ends here


# report the results of the mission
robotArm.report()

# want help? Unlock code below!
# robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

