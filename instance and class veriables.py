class emp:
    leaves = 10

aman = emp() 
samir = emp() 
aman.name = "aman sahu"
samir.name = "samir sahu"
aman.salary = 1000
samir.salary = 1000

print("leaves initialize by emp",emp.leaves)

samir.leaves = 12
print(samir.__dict__)#we cannot change class veiables by objects 

print("leaves change by samir",emp.leaves)

emp.leaves = 20     #only we can change class veriables by class
print("leaves change by emp",emp.leaves)
