from typing import Generator, Iterable, Iterator


# "Iterable" is a property of a object(char,string,not int) , which can be defines in __iter__() or __getitem__()  and in result it gives Iterator
# "Iterator" is a property of a object in which  __next__() defined already
# the process of iterate called "iteration" 

#___________RULES OF ITERATOR________________
# 1st cumpiler will check conditions for iterate of object(char,string)
# when obj is Iterable cumpiler will run __iter__() func. and genrate iterator
# and when we command __next__() to the Iterator cumpiler will Generate next iterator

# here range is Generator that genrate values 0 to 100 it is only capable to genearte 
# Generators generate values on the fly(at runtime)
# Generator not store value 
# whenever we need this values we can iterate and get value 
def gen(n):
    for i in range (n):
        yield(i)

g = gen(3)
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())