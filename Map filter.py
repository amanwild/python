number = ["22","63","63","12","21","14"]

'''
for item in range(len(number)):     
    number[item] = int(number[item])
    # print(number[item])
number[0]=number[0]+3
print("this is 1st no. + 3 =" ,number[0])'''

# ___________maping gives 2 option first (function that apply on whole list) _____________
# ___________maping gives secomd opt  (where to  apply condition) _____________
# ___________map retuns the object that can be store in list _____________
# syntax of map          num = list(map(what you want,put what convrt))
num = list(map(int,number))
num[0]=num[0]+3
print("this is 1st no. + 3 =" ,num[0])

def sq(x):
    return x*x
def cu(x):
    return x*x*x
def grr(y):    
    return (y>3)

n1=[1,2,3,4,5,6,7]
'''
square= list(map(sq,n1))
print(square)
cube= list(map(cu,n1))
print(cube)'''

func = [sq,cu]
for i,item in enumerate(n1):

    fun= list(map(lambda y:y(item),func))

    print(fun)

#__________________FILTER____SAME AS MAP Filter(FUNCTION(condition) , ITERABLE)

gr =list(filter(grr,n1)) 
print("greater then 3 = ",gr)

#_______________reduce__________________reduce(function,iterabele)

from  functools import reduce

num1 = reduce(lambda x,y :x+y, n1)
num2 = reduce(lambda x,y :x*y, n1)
print("sum of no : ",num1)
print("* of no : ",num2)
