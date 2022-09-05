class emp:
    leaves = 5
    def __init__(self,name,salary,job):
        self.name = name
        self.salary = salary 
        self.job = job
    def pri(self):
        print(f"the name is {self.name} salary is {self.salary} job is  {self.job}   ")   

    #this is type of decorator ie @classmethod
    #when we use @classmethod it gives class not self 
    @classmethod #this is use to avoid self and give access to object for control
    def change_leaves(cls ,newleaves):#cls=class
        cls.leaves = newleaves  

aman = emp("AMAN_SAHU",1000,"HOD")
aman.change_leaves(10)
aman.pri()
print(aman.leaves) 