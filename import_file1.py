#using import we can use imported files variables functions 
#when we use import for an file it import contents of that file as well as executes the all process
# import syntax       import<file name>
# to import only content of file      from <file name>  import<content name>
def sq(a):
    return a*a
def cu(a):
    return a*a*a
b = 5
c = 10


if __name__=='__main__':
    print("this is file 1 in main content")
   

    print(sq(2))
    print(cu(2))

print("this is file 1 out main content",sq(3))
