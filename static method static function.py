class emp:
    #staticmethod is used to avoid class and self  arguments 
    #staticmethod is used for on specific work  
    @staticmethod
    def static(str):
        print("this is static method and my anme is :"+str)

sahu = emp()
#we can use static method from class and instance
sahu.static("Aman sahu")
#we can use static method from class and instance
emp.static("Aman sahu")
