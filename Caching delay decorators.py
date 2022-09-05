import time
from functools import lru_cache

# we are using here lru_cache that 
# helps us in multiple time called any task ,it store particular no. 
# of  calls for and then calls the function

@lru_cache(maxsize =2 )#here cache store 2 calls 
def task(n):#note n value does not repeatr
#some code that takes n sec time
    time.sleep(n)
    return n

if __name__=='__main__':
    print("task started")
    task(2)
    task(1)
    print("task (4) complete")
#when input value of  n will be repeat lru_cathe will directly gives result
# cause same input will already exist in cache, this is process 
    task(3)
    print("task (5) complete")
  
