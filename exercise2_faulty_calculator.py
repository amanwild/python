n1 = int(input(" enter first no."))
n2 = int(input(" enter second no."))
print(" \n press [1] for addition\n"
" press [2] for subtraction\n press [3] for multiplication\n "
"press [4] for divition")
o = int(input())

if n1==56 and o==1 and n2==9:
    print("77")
elif n1==45 and o==1 and n2==3:
    print("555")
elif n1==56 and o==4 and n2==4:
    print("4")
elif o==1:
    print( n1 + n2)
elif o==2:
    print( n1 - n2)
elif o==3:
    print( n1 * n2)
elif o==4:
    print( n1 / n2)
else:
    print("invalid choice")


