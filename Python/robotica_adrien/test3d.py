from spatialmath import *
from math import pi

Rx=SO3.Rx(pi/2)
#print(Rx)
Ry = SO3.Ry(pi/2)
#print(Ry)
Rz=SO3.Rz(pi/2)
#print(Rz)
Rxyz=Rx*Ry*Rz
print(Rxyz)
Rxyz= Rx*Rz*Ry 
print(Rxyz)