num=[16,52,23,46,15,27,32]
print("the list is :",num)

num.sort()
print("sorted list is :",num)

print("2nd no.in list is :",(num[1]))

print("num length is :",len(num))
print(num[:7:2])
print()
num.reverse()
print("reverse list is :",num)
print()
num.append(24)
num.append(9)
num.append(15)
print(num)

num.insert(1,12)
num.insert(0,10)

print("this is insert (12,10) function :",num)
num.remove(27)
print("this is remove (27) function :",num)
num.pop()
print("this is pop statement :",num)

tp=(46,6,5,62,6)
print("this is tuple statement :",tp)

a=10
b=20
print("this is befor swaping statement a=",(a)," b=",(b))
a,b = b,a
print("this is after swaping statement a=",(a)," b=",(b))

print()

