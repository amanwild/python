def time():
    import datetime
    return datetime.datetime.now()

def work(nm, main,do):
     if nm == 1:#choose (1)aman ,(2)samir ,(3)rajesh
         if main == 1:#choose (1) log or (2) look
             if do ==1:#(1) exercise , (2) food
                 with open ("aman_ex.txt","a") as op:

                    op.write("\n"+str([str(time())])+" : "+str(input(" what you have exercise ? ")))
                  

                    # op.write([time()],str(input(" what you exercise now: ")))
                    op.close()
                    print("!!! note down successfull !!!")
             elif do ==2:#(1) exercise , (2) food
                 with open ("aman_eat.txt","a") as op:

                    op.write("\n"+str([str(time())])+" : "+str(input(" what do you eat ? ")))
                    
                    op.close()
                    print("!!! note down successfull !!!")
         elif main == 2:#choose (1) log or (2) look1
             if do ==1:#(1) exercise , (2) food
                 with open ("aman_ex.txt") as op:
                    print(op.read())
                    op.close()
             elif do ==2:#(1) exercise , (2) food
                 with open ("aman_eat.txt") as op:
                    print(op.read())
                    op.close()
     elif nm == 2:#choose (1)aman ,(2)samir ,(3)rajesh
         if main == 1:#choose (1) log or (2) look
             if do ==1:#(1) exercise , (2) food
                 with open ("samir_ex.txt","a") as op:

                    op.write("\n"+str([str(time())])+" : "+str(input(" what you have exercise ? ")))
                  

                    # op.write([time()],str(input(" what you exercise now: ")))
                    op.close()
                    print("!!! note down successfull !!!")
             elif do ==2:#(1) exercise , (2) food
                 with open ("samir_eat.txt","a") as op:

                    op.write("\n"+str([str(time())])+" : "+str(input(" what do you eat ? ")))
                    
                    op.close()
                    print("!!! note down successfull !!!")
         elif main == 2:#choose (1) log or (2) look1
             if do ==1:#(1) exercise , (2) food
                 with open ("samir_ex.txt") as op:
                    print(op.read())
                    op.close()
             elif do ==2:#(1) exercise , (2) food
                 with open ("samir_eat.txt") as op:
                    print(op.read())
                    op.close()
     elif nm == 3:#choose (1)aman ,(2)samir ,(3)rajesh
         if main == 1:#choose (1) log or (2) look
             if do ==1:#(1) exercise , (2) food
                 with open ("rajesh_ex.txt","a") as op:

                    op.write("\n"+str([str(time())])+" : "+str(input(" what you have exercise ? ")))
                  

                    # op.write([time()],str(input(" what you exercise now: ")))
                    op.close()
                    print("!!! note down successfull !!!")
             elif do ==2:#(1) exercise , (2) food
                 with open ("rajesh_eat.txt","a") as op:

                    op.write("\n"+str([str(time())])+" : "+str(input(" what do you eat ? ")))
                    
                    op.close()
                    print("!!! note down successfull !!!")
         elif main == 2:#choose (1) log or (2) look1
             if do ==1:#(1) exercise , (2) food
                 with open ("rajesh_ex.txt") as op:
                    print(op.read())
                    op.close()
             elif do ==2:#(1) exercise , (2) food
                 with open ("rajesh_eat.txt") as op:
                    print(op.read())
                    op.close()

name = int(input("Press 1 for Aman \nPress 2 for Samir \nPress 3 for Rajesh \n"))
wo = int(input("Press 1 for log \nPress 2 for retrive \n"))
do = int(input("Press 1 for exercise \nPress 2 for food \n"))
work(name,wo,do)