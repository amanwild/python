a = "aman"
b=a
# == value equality
# is reffrence equality
# now
print(a==b)
print(b is a)
print(a is b)
print(b == a)
print(a == b)

x = [1,2,3]
y=x
print(y is x)
print(x is y)

p = [1,2,3,4]
q = p[:]
print(p)
print(q)
print(p is q)
print(q is p)
q[0] = 4
print(p)
print(q)

