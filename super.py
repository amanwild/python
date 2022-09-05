#__________________Rules of super function_________________________________
# ek bar jo override ho jata h vo run nahi hoti hai 
# override function ko use krne ke liye super().__init__ ka use krte h

#we can call perticular func of  base class by super().<func_name()>
#we can call whole constructor of  base class by super().__init__()

#when we write 1st super function for base class at derived class 
#cumpiler will go to the overrided init base class by super().__init__ and then 
#went back to derived class and exicute init of derived class

#when we write super function at the last for base class at derived class 
#cumpiler will exicute init of derived class 1st and then 
#cumpiler will go to the overrided init base class by super().__init__ 

class base:
    var = "base var"
    def __init__(self):
        print(f"this is base class init function is call {self.var} ")
        print(f"this is base class {self.var} ")
    def special(self):
        print(f"this is special function")

class derived(base):
    var = "derived var"
    def __init__(self):
        print(f"this is derived class init function is call {self.var} ")
        super().__init__()
        print(f"this is after super function  {self.var} ")
        super().special()

aman = derived()
print(aman.var)






