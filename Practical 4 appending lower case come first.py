#____________ NAME : Aman Tikaram Sahu________
# ____________Roll No. : 24___________________
# ____________Std. ID : JBTECH19031___________

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
