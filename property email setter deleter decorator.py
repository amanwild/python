class info:
    def __init__(self , fname,lname):
        self.fname = fname
        self.lname = lname
        
    def pri(self):
        print(f"Name is {self.fname} Sername is {self.lname} ")

# note when we use @property it converts function to property and property no need to add () for calling
    @property
    def email(self):
        print(f"email is  {self.fname}.{self.lname}@gmail.com")
#this is syntax for hiding and to show retype msg after deletion of email
        if self.fname==None or self.lname==None:
            print("email is not set please set using setter ")
            
#this is is syntax to set value of property 
    @email.setter
    def email(self,str):
        print("setting now..")
        name =  str.split("@")[0]
        self.fname =  name.split(".")[0]
        self.lname = name.split(".")[1]

#this is is syntax to del value of property 
    @email.deleter
    def email(self):
        self.fname =  None
        self.lname = None


    @classmethod
    def spl(cls,str):
        return cls(*str.split(" "))

aman = info.spl("AMAN SAHU")
#here we are using () beacuse this is encapsulation
aman.pri()
aman.email
print()

ama = info("ama" ,"sah")
ama.pri()
ama.email
print()

# note when we use @property it converts function to property and 
# property no need to add () for calling
#we have to remove () from function when we are assinging value to property
#() is used for functions
ama.fname = "sahu"
ama.lname = "aman"
ama.pri()
ama.email
print()

#syntax for email set
ama.email = "moin.shah@gmail.com"
ama.pri()
ama.email

print()
#syntax for email deletion 
del ama.email
ama.email

print()
#syntax for email set
ama.email = "pravin.chaudhry@gmail.com"
ama.pri()
ama.email