with open("aman.txt") as file: #if we use with keyword for opening file 
    a = file.read(4)           #then there is no need to close the file
    print(a)
