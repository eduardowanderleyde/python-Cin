from spatialmath import *
from math import pi

Tx=SE3.Tx(1)
Ty=SE3.Ty(2)
Tz=SE3.Tz(3)
Txyz=Tx*Ty*Tz
print(Txyz)

a=[1,0,0]
a_t=Txyz*a
print(a_t)