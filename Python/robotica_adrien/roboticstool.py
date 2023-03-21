from spatialmath import *
from math import pi
import roboticstoolbox as rtb

robot = rtb.models.DH.Planar2()
print (robot)

robot.plot(robot.qr)
input ("press enter")

T1 = robot.fkine([0,0])
print(T1)

T2 = robot.fkine([pi/4,pi/4])
print (T2)

##########
solution1=robot.ikine_LM(T1)
q1=solution1[0]
print(q1)

solution2=robot.ikine_LM(T2)
q2=solution2[0]
print(q2)

T3=SE3(0.3031,11.707,0)
solution3= robot.ikine_LM(T3)
print(solution3)
