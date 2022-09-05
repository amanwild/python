#using import we can use imported files variables functions 
#when we use import for an file it import contents of that file 
# as well as executes the all process

# import syntax       import<file name>
# to import only content of file      from <file name>  import<content name>


from import_file1 import cu ,b ,c #here when we declare import content then 
# no need to write like import_file1.cu ,we can directly access cu

import import_file3#here when we declare import file then 
# there is need to write like import_file1.avg ,we cannot directly access avg

s = "aman is good boy"
import_file3.avg(5,3,7)
import_file3.str(s)
print("this is file 3  content  ie avg  = ",import_file3.avg(2,4,6))
# x=4
# print(__name__)
print("this is file 1  content  ie cube  in file 2= ",cu(4))
print("this is file 1  content  ie b+c in file 2= ",b+c)
print("this is files 2 content ")