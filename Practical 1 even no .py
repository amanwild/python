#____________ NAME : Aman Tikaram Sahu________
# ____________Roll No. : 24___________________
# ____________Std. ID : JBTECH19031___________
start = int(input("Enter the start of range : "))
end = int(input("Enter the end of range : "))

for num in range(start,end + 1):
    if num % 2 == 0:
        print(num,end=" ")