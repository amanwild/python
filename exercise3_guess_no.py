print("!!! guess the no. game !!! ")
print("!!! you have only 9 chance !!! ")

int1=5
while(1):
    print(" you have ",int1," chance")
    num = int(input())
    if num<25 and int1!=0:       
        print("type greater no.")        
    if num>25 and int1!=0:       
        print("type lesser no.")        
    if num==25 and int1!=0:
        print("!!!! you guess the correct no. !!!!")
        break
    int1=int1-1
    if int1==0:
            print("!!!! game over !!!!")        
            break









