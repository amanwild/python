class a:
    def pri():
        print("this is class A")
class b(a):
    def pri():
        print("this is class B")
    # pass
class c(a):
    def pri():
        print("this is class C")
    # pass

#cumpiler will go to the 1st variable 
# which is given by user in class d(1st , 2nd)

class d(c,b):
        print("this is class d")
        # pass
       

A = a()
B = b()
C = c()
D = d()
d.pri()
