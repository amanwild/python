ls = []
for i in range (10):
    if i%3==0:
        ls.append(i)
print(ls)
#this above code ,we can convert it in 1 line 
# by using comprihensing 

# list  comprihensing 
lst = [i for i in range (10) if i%3==0 ]
print("this is lists",lst)

# list  comprihensing 
lst2 = [i for i in ["aman" , "sahu","samir" ,"sahu","rajesh","sahu"]]
print("this is lists",lst2)

# Set comprihensing 
sets = {i for i in range (10) if i%3==0 }
print("this is sets",sets)

# Set comprihensing set does not repeat objects
sets = {i for i in ["aman" , "sahu","samir" ,"sahu","rajesh","sahu"]}
print("this is sets",sets)

# dictionary  comprihensing 
dic = {f"key {i} ":f"items {i}"for i in range (10) if i%3==0 }
print("this is dictionary ",dic)

# reverse dictionary  comprihensing 
dic = { item : key for key,item in  dic.items() if i%3==0 }
print("this is reverse dictionary",dic)

# generator   comprihensing 
evens = (i for i in range (5) ) 
# when i iterate evens by for loop or __next__
#  it will stop at 
# and i cannot iterate that again ,that is generator
print(i)
for i in evens:
    print(i)

# print(evens.__next__())
# print(evens.__next__())
# print(evens.__next__())
# print(evens.__next__())
# print(evens.__next__())
