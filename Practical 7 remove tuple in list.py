#____________ NAME : Aman Tikaram Sahu________
# ____________Roll No. : 24___________________
# ____________Std. ID : JBTECH19031___________
y=[('aman','12CS039'),('samir','12CS320'),('rajesh','12CS055'),('nishu','12CS100')]
low=int(input("Enter lower roll number (starting with 12CS):"))
up=int(input("Enter upper roll number (starting with 12CS):"))
l='12CS0'+str(low)
u='12CS'+str(up)
p=[x for x in y if x[1]>l and x[1]<u]
print(p)
