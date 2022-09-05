list1=[1,2,4,7]
list1.sort()

for items in list1:
    print(items)

list = [["aman","sahu"],["ama",553],["am",6233]] 
for item,lollypop in list:
    print(item ," lollypop is ", lollypop)
print()

for item,value in list:
    print(item ," sername is ")
  
print()
dic=dict(list)
print(dic)

print()
for item in dic:
    print(item ," sername is ")
print()

for item,lollypop in dic.items():
    print(item ," is lollypop ", lollypop)

list3 =[3222,626,"ggdgg","dgd","er",313,22,30303,2,3,3]
print()
for abc in list3:
    print(str(abc).isnumeric() and abc>=6)

    if str(abc).isnumeric() and abc>=6:
        print(abc)




