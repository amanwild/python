class foot :
    str1 ="foot class"
#note here when we call def func it takes object as self automaticaly 
    def foo(self):
        print(f"My class name is {self.str1} this is base class of ")
        return 0

class  ball (foot):
    str2 =" ball class"
#note here when we call def func it takes object as self automaticaly 
    def bal(self):
        print(f"My class name is {self.str2} derived from {self.str1}")
        return 0
#this is syntax of multilevel inheritance
class  player (ball):
    str3 =" player class"
#note here when we call def func it takes object as self automaticaly 
    def ply(self):
        print(f"My class name is {self.str3} derived from {self.str2}")
        return 0

f = foot()
b = ball()
p = player()
p.foo()
p.bal()
p.ply()