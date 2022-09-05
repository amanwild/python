class emp:
    def __init__(se,name,salary,job):
        se.name = name
        se.salary = salary
        se.job  = job 
    def pri(se):
        print(f"name is {se.name} salary is {se.salary} job is {se.job} ")
    @classmethod
    def spl(cls , str):
        return cls(*str.split(" "))

 
#this is syntax of single inheritance
class emp2(emp):
    #we can create classmethods as well as instancemethods in inheritance class
    def __init__(se,name,salary,job,lang):#here we can use super statement also but in another code we are used  
        se.name = name
        se.salary = salary
        se.job  = job 
        se.lang = lang
    def pri(se):
        print(f"name is {se.name} salary is {se.salary} job is {se.job} and language is {se.lang} ")

aman = emp ("aman",1000,"hod")
aman.pri()

samir = emp.spl("samir 1000 head")
samir.pri()

sahu = emp2("ama", 50 , "watch", ["java cpp"])
sahu.pri()