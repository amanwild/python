i=0
while(True):
    if i+1<=5:
        i=i+1
        continue
    print(i,end= " ")
    if i>=45:
        break
    i=i+1

while(True):
    po = int(input("\nenter the no. less than 100 and greater than 10 to continue : "))
    if po<=10:
        po=po+1
        continue
    print(po , end=" ")
    po=po+1
    if po>100:
        print()
        print("\ncongrates !!!! ")
        break



