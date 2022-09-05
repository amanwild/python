nm = "aman"
sn = "sahu"

a = "this is %s \n"%nm
c = "this is %s "%sn
print(a,c)

a1 = "this is %s %s" %(nm ,sn)
print(a1) 

b = "this is {} {} " 
b1 =b.format(nm ,sn)
print(b1)

b = "this is {1} {0} " 
b1 =b.format(nm ,sn)
print(b1)

import math
c = f"this is {nm} {sn} = {5*7} {math.sin(90)}" #this is fstring formatting
print(c)