# in decorator we use function as an argument to another function

def dec1 (take1):#after assinging take1 function in dec1 
    #take1 functions change to dec2 means dec1 + take1 = dec2
    def dec2():
        print("hello guys")
        take1()
        print("bye bye guys")
    return dec2 #we can return as well function also

@dec1      #we have 2 methods for decoration 1st is this type 
# here @ asign its below function to @(funtion) ie dec1
def take1():
    print("this is aman sahu here")

# take1 = dec1(take1)#__________________________and 2nd type is this 
take1()