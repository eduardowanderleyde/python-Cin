import roboticstoolbox as rtb
from math import pi
from spatialmath import SE3

robot = rtb.models.DH.Planar2()
print (robot)

robot.plot(robot.qr)
input ("press enter")

# T1 = robot.fkine([0,0])
# print(T1)

# T2 = robot.fkine([pi/4,pi/4])
# print (T2)