# methods which are start and end with "__" called dunder methods. Ex. __init__ 
class emp :
    def __init__(self,name  ,sername,salary):
        self.name = name
        self.salary = salary
        self.sername = sername
        
    def pri(self):
        print(f"Name is {self.name} Sername is {self.sername} Salary is {self.salary}")

#dunder methods are available on google mapping operators to function
#here __add__ dunder method is used to add name and sername
    def __add__(self,other):
        return self.name + " " +other.sername
    @classmethod
    def spl(cls,str):
        return cls(*str.split(" "))

# when __repr__ and __str__ both dunder method are present in class 
# then priority get to str then repr dunder
    def __repr__(self):
        return f"Name is {self.name} Sername is {self.sername} Salary is {self.salary} from repr"
    def __str__(self):
        return f"Name is {self.name} Sername is {self.sername} Salary is {self.salary} from str"
    

am = emp.spl("AMAN SAHU 100")
mo = emp.spl("MOIN SHAH 200")
am.pri()
mo.pri()
print(am + mo)
print(mo + am)
# syntax to call defaul str 
print(am)
# syntax to call defaul repr
print(repr(mo))

