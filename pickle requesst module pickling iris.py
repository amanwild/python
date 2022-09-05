import requests
# import pickle

print("data")
data = requests.get("http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").text
print(data)

# l1 = data.split("\n") 
# l2 =[item for item in l1 if item.len != 0 ]
# # l1 =[item.split(" ") for item in l1]

# print(l2)

# open with ("pickle.pkl","wb") as f
