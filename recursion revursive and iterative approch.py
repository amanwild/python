def factorial(n): #factorial by recursive function
 
    for i in range(n):
         if n==1:
      
            return 1
         else :
           return n * factorial(n-1) 

def factorial1(n):#factorial by iterative function
    f=1
    for i in range(n):
         f = f * (i+1)
    return f

def fibonacci(n):
    
     if (n==2):
         return 1
     elif (n==1):
         return 1
     else:
         return fibonacci(n-1)+fibonacci(n-2)
   
    


num = int(input("enter any no. to find factorial :"))
print("factorial is :",factorial(num))
print("factorial is :",factorial1(num))
print("fibonacci is :",fibonacci(num))





