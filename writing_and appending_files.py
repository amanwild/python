f= open("aman.txt","a") #a is used of adding(append) new lines w is used to write only current line
# f= open("aman.txt","w") #a is used of adding(append) new lines w is used to write only current line
f.write("aman is good boy "
"and smart boy\n")
f.close()

f2=open("aman.txt","r+")# r+ is used for both read and write
con = f2.read()
f2.write("thnk you\n")
print(con)
f2.close()