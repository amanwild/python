a=200#________________________this is global veriables
print(a," this is in global")

def func1():
    a=10#________________________this is local  veriables
    print(a," this is in local")

def func2():
    a=20#________________________this is local  veriables
    print(a," this is in local\n")
    def func3():
        a=30#________________________this is local  veriables
        print(a," this is in func2 /func3 locallocal\n")
    func3()
    
def func4():
    b=20#________________________this is local  veriables
    def func5():
        global b#________________________this is global veriables
        b=300#________________________this is global  veriables
        # print(b," this is in locallocal\n")
    print(b," this is in local\n")
    func5()
    print(b," this is in local\n")
func1()
func2()
func4()
#________________________this is global veriables
print(b," this is in global")









