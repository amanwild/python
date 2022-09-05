from typing import ItemsView


def sem(normal,*args,**kwarg):
    print(normal)
    for i in  args:
        print(i)
    for key,value in kwarg.items():
        print(f"this is name = {key}  and this is sername = {value} ")

normal = "welcome to sem function\n"

args=("aman","samir","rajesh")
kwargs={"aman":"wild","samir":"sahu","rajesh":"shah"}
sem(normal,*args,**kwargs)

