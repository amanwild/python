import time 
ini = time.time()
i =0
while i<45:
    time.sleep(.1)
    i+=1
    print(f"aman sahu is a good boy({i}) ")
print(f"while loop complete in {time.time()-ini} seconds ")
ini1=time.time()
i =0
print()
for i in range (45):
    time.sleep(.1)
    i+=1
    print(f"aman sahu is a good boy({i}) ")
print(f"for loop complete in  {time.time()-ini1} seconds ")
print()

local_time= time.asctime(time.localtime(time.time()))
print(f"current time is  {local_time}  ")