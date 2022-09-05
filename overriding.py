#rules of OVERRIDING 
# ek bar jo override ho jata h vo run nahi hoti hai 
#when we call a ambiguity funcion which is may be present in derived class ,derived init ,base class ,base init
# then compiler follow this path
# 1st compiler will search function in derived (init) if there is not found then 
# 2nd compiler will search function in base class if there is not found then 
# 3rd compiler will search function in derived (init) if there is not found then 
# 4th compiler will search function in base class .

# priority of compiler are:
# (1)derived init, (2)base init,(3)derived class,(4)base class
# ek bar jo override ho jata h vo run nahi hoti hai
class base:
    var = "base var"
    def __init__(self):
        var = "base init var"
        print(f"this is base class init function is call")
        print(f" this is base class {self.var} ")
# override function ko use krne ke liye super().__init__ ka use krte h
class derived(base):
    var = "derived var"
    def __init__(self):
        var = "derived init var"
        print(f"this is derived class init function is call")
        print(f" this is derived class {self.var} ")

aman = derived()
print(aman.var)