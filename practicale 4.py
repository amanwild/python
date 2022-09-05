from statistics import median
user = int(input( "How many numbers you have?")) 
total = []
for n in range(user): 
    number = float(input("Enter the numbers: ")) 
    total.append(number) 
print('Median of following number is: ',median(total))
