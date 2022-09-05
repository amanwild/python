import pickle

#  #pickling a python object
# name = ["aman","sahu","samir","rajesh"] #it may be any obj of python
# file = "names.pkl"
# files = open(file,"wb") #it takes 1 obj file and condiotion write binary
# obj1 = pickle.dump(name,files)

file = "names.pkl"
files = open(file,'rb') #it takes 1 obj file and condiotion read binary
myname = pickle.load(files)
print(myname) 
