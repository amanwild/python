class emp:
    cha ="emp class"
    def __init__(self,name,salary,job):
        self.name = name
        self.salary = salary
        self.job  = job 
    def pri(self):
        print(f"name is {self.name} salary is {self.salary} job is {self.job} ")
    @classmethod
    def spl(cls , str):
        return cls(*str.split(" "))

class player:
    cha ="player class"
    def __init__(self,name,game):
        self.name = name
        self.game = game
    def pri(self):
        print(f"player name is {self.name} game is {self.game} ")

#this is syntax of multiple inheritance
#in syntax (1st,2nd) 1st class will execute first and then 2nd
class coolprog(emp,player):
#in multilevel parent class 1st class will completly executed
#we can create classmethods as well as instancemethods in inheritance class
    lang = "cpp"
    def prilang(self):
        print(self.lang)


aman = emp ("aman",1000,"hod")
aman.pri()

samir = emp.spl("samir 1000 head")
samir.pri()

rajesh = player("raj","football")
rajesh.pri()


sahu = coolprog("aman",999,"football")
sahu.pri()
sahu.prilang()

#when same instance is call which is present in both parent class
#by default cumpiler take 1st class which is mentioned in coolprogie.
print(sahu.cha) 
