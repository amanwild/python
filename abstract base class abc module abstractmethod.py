from abc import ABC, abstractmethod
class shape(ABC):
#this abstractmethod force to derived(child) class to must define/empliment particular function
#we cannot create obj of abstract base class directly
    @abstractmethod
    def pri():
        return 0

class rect(shape):
    def __init__(se):
        se.l = 10 
        se.b  = 5
    def pri(se):
        return se.l * se.b 

class sq(shape):
    def __init__(se):
        se.l = 10   
    def pri(se):
        return se.l * se.l
r = rect()
print("area of reactangle is ",r.pri())
s = sq()
print("area of square is ",s.pri())
