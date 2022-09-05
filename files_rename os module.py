import os
print(os.getcwd())
# for i in range (20):
#     os.mkdir(f"aman{i}")

def renm(pth):
    os.chdir(pth)
    print(os.getcwd())
    for i in range (20):
        os.rename(f"aman{i}",f"Sahu{i}")
# def cap(pth):
#      os.chdir("pth")
    # print(os.getcwd())

if __name__=='__main__':
    print("enter the path you want to change file name and capatilize")
    pth = input()
    renm(pth)
    # cap(pth)
























