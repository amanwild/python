# introspection is getting information about object 
#in python everything is obj
class info:
    def __init__(self , fname,lname):
        self.fname = fname
        self.lname = lname
        
    def pri(self):
        print(f"Name is {self.fname} Sername is {self.lname} ")

aman = info ("aman","sahu")
# print(type())
# . means class 
# __<name>__ means dunder methods
#type gives type
print(type(aman))
#id gives id
print(type("aman"))
#id gives id
print(id("aman"))
#dir gives what we can do with obj
print("these all we can do with aman ",dir(aman))