from RobotArm import RobotArm

robotArm = RobotArm('exercise 2')
# Jouw python instructies zet je vanaf hier:
robotArm.grab()
for i in range(9,0,-1):
    i * robotArm.moveRight()
robotArm.drop()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()