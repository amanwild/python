import random
lst =  ["s","w","g"]
at = 10
us = 0 
# i = 0
cs = 0
while(10>=at and 0!=at):
    print(f"\t\t you have ({at}) attemp")
    uin = (str(input("Enter your choice [ (s)snack (w)water (g)gun ] :  ")))
    u = uin.lower()
    c = random.choice(lst)
    print()
    # if u!="s" and u!="w" and u!="g":  
    #     print("!!! Invalid Input !!!")
    #     continue      
    # if u=="s" or u=="w" or u=="g":        
    if u=="s" and c=="w":
            us += 1
            print(f" You win   ||    ({u})You = {us} , ({c})Computer = {cs} ")
    elif u=="w" and c=="g":
        us += 1
        print(f" You win   ||   ({u})You = {us} , ({c})Computer = {cs} ")
    elif u=="g" and c=="s":
        us += 1
        print(f" You win   ||    ({u})You = {us} , ({c})Computer = {cs} ")
    elif u==c:
        print(f" TIE   ||    ({u})You = {us} , ({c})Computer = {cs} ")
        continue
    else:
            cs += 1
            print(f" Computer win    ||    ({u})You = {us} , ({c})Computer = {cs} ")
    at =at - 1
    print()
   
if u>c:
    print(f"Congratulation !!! You are Winner  SCORE: You({us}) Comuter({cs})") 
else:
    print(f"Computer Win !!! You are Loser  SCORE: You({us}) Comuter({cs})")           
print()



