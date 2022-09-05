#____________ NAME : Aman Tikaram Sahu________
# ____________Roll No. : 24___________________
# ____________Std. ID : JBTECH19031___________
test_keys = ["Rash", "Kil", "Varsha"]
test_values = [1, 4, 5]
# Printing original keys-value lists
print ("Original key list is : " + str(test_keys))
print ("Original value list is : " + str(test_values))
# using dictionary comprehension
# to convert lists to dictionary
res = {test_keys[i]: test_values[i] for i in range(len(test_keys))}
# Printing resultant dictionary
print ("Resultant dictionary is : " + str(res))