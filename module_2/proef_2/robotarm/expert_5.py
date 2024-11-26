from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.expert import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[5],0)
# your code starts here:
red=0
yellow=0
blue=0
lijst=[]
robotArm.moveRight()
robotArm.grab()
kleur=robotArm.scan()
robotArm.drop()
for x in range(8):
    robotArm.moveRight()
    robotArm.grab()
    coller =robotArm.scan()
    robotArm.drop()
    print(coller)
    if coller =="red":
        red+=1
    elif coller== "yellow":
        yellow+=1
    else:
        blue+=1



print(red)
print(yellow)
print(blue)

a=9
b=8

if red > yellow and red > blue:
    grootste = "red"
elif yellow > red and yellow > blue:
    grootste = "yellow"
elif blue>yellow and blue>red:
    grootste = "blue"
else: 
    grootste=kleur
    

print(f"the bigest coller is: {grootste}")
for x in range(9):
    robotArm.grab()
    chek= robotArm.scan()
    if chek == grootste:
        for y in range(a):
            robotArm.moveLeft()
        robotArm.drop()
        for y in range(b):
            robotArm.moveRight()
            
    else:
        robotArm.drop()
        robotArm.moveLeft()
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

