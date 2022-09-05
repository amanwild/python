import os
# print(os.getcwd())
# os.chdir("d:/a_sample.txt")
# print(os.getcwd())
# # os.mkdir("a_sample.txt/b_sample.txt")

# file= open("b1.txt","w") 
# file.write("this is amn sahu")

# # os.makedirs("aman/sahu")
# location = "D://a_sample.txt/aman"
# # os.chdir("D://a_sample.txt/aman")
# print(os.getcwd())
# file = 'sahu'
# path=os.path.join(location,file)

# os.remove(path)

# os.rename("sahu")
# os.remove("D://a_sample.txt/aman/sahu")

# print(os.path.exists("D://a_sample.txt/aman/sahu"))

#__________________to delete the file

os.chdir("D:/a_sample.txt/aman")

location = "D:/a_sample.txt/aman"
file = 'aman'
path = os.path.join(location,file)

os.remove("D:/a_sample.txt/aman/sahu")
