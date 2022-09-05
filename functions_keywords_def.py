def my():
    print("welcome to my world")

def avg_no_return(a,b):
    """it's ans will none couse this function no return any thing
                  and this is doc string """
    print(((a+b)/2)) #when any function not return any thing we can store in veriables 

def avg(a,b):
    return ((a+b)/2)

my()
my()
print("avg of 5 , 7 is  ",avg(5,7))

st = avg(16,8)
print()
print("avg of 16 , 8 is  ",st)

print()

print("avg of 20 , 10 is  ",(avg_no_return(20,10)))
print()

print(avg_no_return.__doc__)#this is used to see what is work of perticular function(doc string)

print()

