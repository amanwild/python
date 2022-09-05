#____________ NAME : Aman Tikaram Sahu________
# ____________Roll No. : 24___________________
# ____________Std. ID : JBTECH19031___________
def recursive(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else :
        return num + recursive(num - 1)    

num = 10
print(recursive(num))

