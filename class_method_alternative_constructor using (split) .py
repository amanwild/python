# from _typeshed import Self


class emp:
    leaves = 5
    def __init__(self,name1,salary1,job1):
        self.name =name1
        self.salary =salary1
        self.job  =job1 
    def pri(self):
        print(f"name is {self.name} salary is {self.salary} job is {self.job}  ")
  
    @classmethod#when use clss method 1st argument always class ie. cls
    def change_leaves(cls ,newleaves):
        cls.leaves=newleaves

    @classmethod
    def constructor(cls,string):#when use clss method 1st argument always class
        params = string.split(" ")#this statement converts string to list
        # after using class method return value to class 
        return cls(params[0],params[1],params[2])#this gives value address to emp
   
    @classmethod
    def constructor2(cls,string):#this is another method to pass the arguments 

        return cls(*string.split(" "))#this gives value address to emp

aman = emp("aman",1000,"hod")
moin = emp("moin",10,"loffer")

aman.pri()
moin.pri()

print(moin.name)
print(moin.salary)
print(moin.job)


aman.change_leaves(10)
print("new leaves are :",aman.leaves)

#this emp.constructor command directly send argument to class not self
#coause classmethod is used here
samir = emp.constructor("samir sahu Good")#here new obj is created 
print(samir.name)
print(samir.salary)
print(samir.job)

# this is anothe method of giving arguments to class
harsh = emp.constructor2("Harsh Meshram Good")
harsh.pri()



