while(True): 
    print("for add press 1")
    print("for sub press 2")
    print("for mul press 3")
    print("for div press 4")
    print("for exit press 5")
    print()
    input_value = int(input())
    if (input_value == 1):
        print("enter two no. for add")
        num1 = int(input())
        num2 = int(input())
        if((num1 == 56 and num2 == 9) or (num2 == 56 and num1 == 9)):
            print("add of ", num1," and ",num2," is : " ,'77')
        else:
            print("add of ", num1," and ",num2," is : " ,(num1+num2))
            print()
        
    if (input_value == 2):
        print("enter two no. for sub")
        num1 = int(input())
        num2 = int(input())
        print("sub of ", num1," and ",num2," is : " ,(num1-num2))
        print()
        
    if (input_value == 3):
        print("enter two no. for mul")
        num1 = int(input())
        num2 = int(input())
        if((num1 == 45 and num2 == 3) or (num2 == 45 and num1 == 3)):        
            print("mul of ", num1," and ",num2," is : " ,'555')
        else:
            print("mul of ", num1," and ",num2," is : " ,(num1*num2))
            print()
        
    if (input_value == 4):
        print("enter two no. for div")
        num1 = int(input())
        num2 = int(input())
        if((num1 == 56 and num2 == 6) or (num2 == 56 and num1 == 6)):        
            print("div of ", num1," and ",num2," is : " ,'4')
        else:
            print("div of ", num1," and ",num2," is : " ,(num1/num2))
            print()
        
    if (input_value == 5):
        break 
            
    
        