#____________ NAME : Aman Tikaram Sahu________
# ____________Roll No. : 24___________________
# ____________Std. ID : JBTECH19031___________
class Vehicle:
    def __init__(self,name,mileage):
        self.name=name
        self.mileage=mileage
    def final(self):
        print(f"vehicle name: {self.name} ; vehicle mileage: {self.mileage}")
class bus(Vehicle):
    pass
school_bus = bus("volvo",20)
print("bus name and mileage is: " ,school_bus.name,school_bus.mileage)
school_bus.final()