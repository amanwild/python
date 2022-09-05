num = int(input("enter any no. :"))
op =int(input("choose any one from 1 or 0 :"))
if op==True:
    for i in range (num): 
        for j in range(i+1):
            print(" + ",end=" ")
        print()  
    for i in range (num):     #another method
        print(" * "*(i+1))  
if op==False:
    for i in range (num,0,-1):  
        for j in range(i):
            print(" + ", end=" ")
        print()
    for i in range (num,0,-1):  #another method
        print(" * "*i) 







