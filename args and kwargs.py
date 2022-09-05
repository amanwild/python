# from typing import KeysView, ValuesView


def funargs(norm,*lst,**kwargs):# *args and **kwargs are optional 
    print(normal+"\nthis is a normal arguments ")
    print("\nthese are boys ")
    print(type(norm)) 
    for key in lst:
        print(key)
    print(type(lst))    # *args are used to directly transfer arguments as a tuple only ()
    print("\nthis is a kwargs ")  
    for key ,value in kwargs.items():
        print(f"{key} sername is {value}")
    print(type(kwargs)) # **kwargs are used to transfer arguments as a dic ie.key pairs {( : )}



normal ="aman is a good boy"
lst =["aman","sahu","ankit","adil","moin","shah"]
kwargs ={"aman":"sahu","ankit":"adil","moin":"shah"}
funargs(normal,*lst,**kwargs)#*args are used to directly transfer arguments as a tuple only ()
