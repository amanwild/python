str = "ComPuTer "
lower = []
upper = []
for s in str:
    if s.islower():
        lower.append(s)
    else:
        upper.append(s)
sorted_str = ''.join(lower+upper)
print("lower case arrangement is done :",sorted_str)