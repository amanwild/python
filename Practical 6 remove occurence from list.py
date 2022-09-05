#____________ NAME : Aman Tikaram Sahu________
# ____________Roll No. : 24___________________
# ____________Std. ID : JBTECH19031___________
a=[]  
n= int(input("Enter the number of elements in list:")) 
for x in range(0,n):
    element=input("Enter element" + str(x+1) + ":") 
    a.append(element) 
print(a) 
c=[]
count=0
b=input("Enter word to remove: ") 
n=int(input("Enter the occurrence to remove: ")) 
for i in a: 
    if(i==b):
        count=count+1
        if(count!=n):  
            c.append(i) 
    else:
        c.append(i)  
if(count==0):
    print("Item not found ") 
else: 
    print("The number of repetitions is: ",count) 
    print("Updated list is: ",c) 
    print("The distinct elements are: ",set(a))
