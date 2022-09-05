#enumarate function gives (index) = no. of items and (items)


li = ["aman","samir","rajesh","shubhm","subhash"]
lis = {"aman":"samir","rajesh":"shubhm","subhash":"yash"}

for index ,item in enumerate(li):#this is impliment of enumerate
    if index%2==0:
        print(f"jarvis please talk to {item}")
print()

#this is impliment of enumerate as well get function for dic
for index ,item in enumerate(lis):
    if index%2==0:
        print(f"jarvis {item} please talk to "+lis.get(f"{item}"))
