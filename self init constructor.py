# :::::::::::::::::::::NOTE:::::::::::::::::::::::::::
# class not takes any arguments remember
# ::::::::::::::::::::::::::::::::::::::::::::::::

class Employee:
    leaves = 10
#this constructor automaticaly executed when object is created
#constructor no need to call from object
# def __init__(argumnts to initialize):
#this is syntax of self initialize constructor  
    def __init__(self,aname,asalary,arole):#this syntax called constructor 
        #here self points to that object 
        # which object is created by this Employee class ie aman ,samir  
        self.name =aname
        self.salary = asalary
        self.role = arole
        print("this is automaticaly run constructor")

    def printdetails(self):
        return f"Name is {self.name} Salary is {self.salary} Role is {self.role} "

aman = Employee("Aman Sahu",1000,"head")
samir = Employee("Samir Sahu",100,"watch" )
# aman.name = "Aman Sahu" 
# aman.salary = 1000
# aman.role = "head"
# samir.name = "Samir Sahu"
# samir.salary = 1000
# samir.role = "head"

print(aman.printdetails())
print(samir.printdetails())
