# Dictionary : key and value pair, unordered, changeable, indexed

# Example 1 : How to create Dictionary
# myDic = {101: "x", 102: "y", 103: "z"}
# print(myDic)  # {101: 'x', 102: 'y', 103: 'z'}

# Example 2 : Accessing item from the Dictionary
# myDic = {
#     "brand": "Tata",
#     "model": "Tiago",
#     "year": 2020
# }
#
# # print(myDic["brand"])  # Tata
# # print(myDic["model"])  # Tiago
#
# # Using get()
# dic = myDic.get("year")
# print(dic)  # 2020

# Example 3 : Change values in the Dictionary
# myDic = {
#     "brand": "Tata",
#     "model": "Tiago",
#     "year": 2020
# }
#
# print(myDic)  # {'brand': 'Tata', 'model': 'Tiago', 'year': 2020}
# myDic["model"] = "Tiago XZ"
# print(myDic)  # {'brand': 'Tata', 'model': 'Tiago XZ', 'year': 2020}

# Example 4 : Reading items from the Dictionary using loop
# myDic = {
#     "brand": "Tata",
#     "model": "Tiago",
#     "year": 2020
# }
# for i in myDic:
#     print(i)  # print only keys from the Dictionary
#     print(myDic[i])  # print only values from the Dictionary
#
# for i in myDic.values():
#     print(i)  # print only values from the Dictionary

# for x, y in myDic.items():
#     print(x, y)   # print keys and values both from the Dictionary

# # Example 5 : Check if key is existing in the Dictionary or not
# myDic = {
#     "brand": "Tata",
#     "model": "Tiago",
#     "year": 2020
# }
# if "model1" in myDic:
#     print("Exist")
# else:
#     print("Not Exist")

# print("model" in myDic)

# Example 6 : Length of Dictionary
# myDic = {
#     "brand": "Tata",
#     "model": "Tiago",
#     "year": 2020
# }
# print(len(myDic))  # 3

# Example 7 : Adding items in to the Dictionary
# myDic = {
#     "brand": "Tata",
#     "model": "Tiago",
#     "year": 2020
# }
#
# myDic["color"] = "white"
# print(myDic)  # {'brand': 'Tata', 'model': 'Tiago', 'year': 2020, 'color': 'white'}

# Example 8 : Remove items from the Dictionary
# myDic = {
#     "brand": "Tata",
#     "model": "Tiago",
#     "year": 2020
# }
# using pop()
# myDic.pop("year")
# print(myDic)  # {'brand': 'Tata', 'model': 'Tiago'}

# using del
# del myDic["year"]
# print(myDic)  # {'brand': 'Tata', 'model': 'Tiago'}
#
# del myDic
# print(myDic)  # NameError: name 'myDic' is not defined

# myDic.clear()
# print(myDic)  # {}

# Example 9 : copy Dictionary
myDic1 = {
    "brand": "Tata",
    "model": "Tiago",
    "year": 2020
}

# Without using copy()
# myDic2 = myDic1
# print(myDic2)  # {'brand': 'Tata', 'model': 'Tiago', 'year': 2020}

# with copy()
# myDic2 = myDic1.copy()
# print(myDic2)  # {'brand': 'Tata', 'model': 'Tiago', 'year': 2020}
