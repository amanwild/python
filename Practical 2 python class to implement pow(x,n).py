#____________ NAME : Aman Tikaram Sahu________
# ____________Roll No. : 24___________________
# ____________Std. ID : JBTECH19031___________
class power:
    def pow(self,x,n):
       print("pow(",x,",",n,") =",x**n)
p = power()
x=int(input("enter 'x' value : "))
n=int(input("enter 'n' value : "))
p.pow(x,n)