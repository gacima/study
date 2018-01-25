import json

jsonString = '{"arrayNums": [{"number": 0}, {"number": 1}, {"number": 2}], "arrayOfFruits": [{"fruit": "apple"}, {"fruit": "banana"},{"fruit": "pear"}]}'
jsonObj = json.loads(jsonString)

print(jsonObj)
print(jsonObj.get("arrayNums"))
print(jsonObj.get("arrayNums")[1])