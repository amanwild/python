import json

data = '{"aman":"sahu","samir":"sahu"}' #it converts string to dictionry
print(data)


parsed = json.loads(data)
print(parsed["aman"])
print(parsed)

data2  = {
    "aman":"sahu",
    "bike":['hero','gadha','activa'],
    "num":['one','two','three'],
    "what" :True,
    "what2" :False
}

#json.dumps to convert code for javascript compatable object
#which is understand by js
jscomp = json.dumps(data2)
print(jscomp)