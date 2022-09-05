#   __privet #this is syntax of privet 
#  _protecte #this is syntax of protecte 
#  public    #this is syntax of public


class home:
#this is Initialization syntax of privet protected public 
#this is declaration syntax of privet protected public 
    __privet = "this privet space "
    _protecte = "this protected space "
    public = "this public space "
    __privet1   =11
    _protecte1  =22
 
    def access(self):
#this is 1st syntax of privet protected public to call
        print(f"this is {self.__privet} ")
        print(f"this is {self._protecte} ")
        print(f"this is {self.public} ")


aman = home()
pub = aman.access()

#this is 2nd syntax of privet protected public to call
print (aman._home__privet1)
print (aman._protecte1)
print (aman.public)
