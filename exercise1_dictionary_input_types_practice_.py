dic ={"aman":"sahu","pravin":"choudary","ankit":"adil","moin":"shah"}
print("enter any name :")
search = str(input())
print(dic.get(search))

name = input("enter the name :")
print(dic.get(str(input())))

name = input("enter the name :")
print(name.lower())

print(dic[name.lower()])