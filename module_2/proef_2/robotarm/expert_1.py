from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.expert import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[1],0)
# your code starts here:

blok=4

for stapel in range(3):
    robotArm.moveRight()
for start in range(4):
    teller=0
    cijfer =5
    for x in range(blok):
        robotArm.grab()
        for y in range(5):
            robotArm.moveRight()
        robotArm.drop()
        for a in range(cijfer):
            robotArm.moveLeft()
        teller+=1
        print(teller)
        if teller== (blok-1):
            cijfer+=1
    blok-=1            


# your code ends here


# report the results of the mission
robotArm.report()

# want help? Unlock code below!
# robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

