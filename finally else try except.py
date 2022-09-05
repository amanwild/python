

try:
    # op = open("aman.txt")
    print("try is running")
except Exception as e:
    print("when try will not running ;except will run",e)
except ArithmeticError as e:
    print("when try will not running ;except will run",e)
else:
    print("when except will not running ,else will run")
finally:
    print("no matter where(in\ try\except or other) finally is ;finally will definatly run")