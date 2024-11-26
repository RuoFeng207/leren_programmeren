from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.expert import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[3],0)
# your code starts here:

a=1

while True:
    chek =robotArm.stackEmpty()
    if chek == True:
        break
    else:
            
        robotArm.grab()
        for y in range(a):
            robotArm.moveRight()
        robotArm.drop()
        for z in range(a):
            robotArm.moveLeft()
        a+=1
        

# your code ends here


# report the results of the mission
robotArm.report()

# want help? Unlock code below!
# robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

