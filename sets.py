s = set()
print(type (s))

print()
l=[623,3,2,6,23,]

print(l)
s1=set(l)
print(type(set(l)))
print()

s2=set()
s2.add(1)
s2.add(2)
print("this is set s2 :",s2)
s3=s2.union({1,2,3,4})
print("this is set s2 :",s2," and set s3 :",s3)
s3.remove(1)
print("this is set s3 :",s3)