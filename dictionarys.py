dic = {"aman":"sahu","samir":"sahu","rajesh":"sahu","ankit":"adil"}
print("my dictionary (show) : ",dic)

dic["pravin"]="chaudhary"
print("addind pravin : ",dic)

dic["24"]="aman"
print("adding aman : ",dic)

del dic["ankit"]
del dic["rajesh"]
print("deleting rajesh ,ankit : ",dic)

print(dic.get("aman"))

dic.update({"25":"ankush"})
print("adding ankush : ",dic)

dic2 =dic.copy()
del dic2["aman"] 
print()
print("after deletion aman with copy",dic)

dic1 =dic
del dic1["aman"] 
print()
print("after deletion aman w/o copy",dic)

dic.update({"aman":"sahu"}) 
print("after adding aman by update function",dic)
print()
print(dic.keys()) #to show all the keys of dic
print()
print(dic.items())

