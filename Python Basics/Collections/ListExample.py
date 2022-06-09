# List - Ordered, changeable, mutable, represents []
#
# Example 1 : How to create list

# myList1 = [10, 20, 30, 40, 50]
# myList2 = ["apple", "banana", "cherry"]
# myList3 = ["apple", 10, "banana", 20]
# myList4 = list()  # empty list
#
# print(myList1)
# print(myList2)
# print(myList3)
# print(myList4)

# Example 2 : Accessing item from the list
# myList = ["apple", "banana", "cherry"]
# print(myList[0])
# print(myList[2])
# print(myList[-1])
# print(myList[-2])

# Example 3 : Range of indexes
# myList = ["apple", "banana", "cherry", "orange", "mango", "melon", "kiwi"]
# print(myList[2:5])  # ['cherry', 'orange', 'mango']
# print(myList[:5])  # ['apple', 'banana', 'cherry', 'orange', 'mango']
# print(myList[-4:-1])  # ['orange', 'mango', 'melon']

# Example 4 : Change item value from the list
# myList = ["apple", "banana", "cherry"]
# print(myList)
# myList[0] = "orange"
# print(myList)

# Example 5 : Read the list item using loop
# myList = ["apple", "banana", "cherry", "orange", "mango", "melon", "kiwi"]
# for i in myList:
#     print(i)

# Example 6 : Check if iem is existing in the list or not
# myList = ["apple", "banana", "cherry", "orange", "mango", "melon", "kiwi"]
# if "apple" in myList:
#     print("Yes.. apple is present")
# else:
#     print("No.. apple is not present")

# Example 7 : List length
# myList = ["apple", "banana", "cherry", "orange", "mango", "melon", "kiwi"]
# lstLen = len(myList)
# print(lstLen)  # 7

# Example 8 : Add item in the List append(), insert()
# myList = ["apple", "banana", "cherry"]
# myList.append("orange")  # adding a new iem at the end of list
# print(myList)
#
# myList.insert(2, "kiwi")
# print(myList)  # adding a new item (somewhere middle of list) at the index place which is given by us

# Example 9 : Remove item from list
# myList = ["apple", "banana", "cherry", "orange", "mango", "melon", "kiwi"]

# using pop()
# myList.pop(0)  # here we specify the index of value
# print(myList)  # ['banana', 'cherry', 'orange', 'mango', 'melon', 'kiwi']

# using del
# del myList[2]
# print(myList)  # ['apple', 'banana', 'orange', 'mango', 'melon', 'kiwi']

# using clear()
# myList.clear()  # Clear all item from the list
# print(myList)  # []

# Example 10 : Copy list from other list
# myList1 = ["apple", "banana", "cherry", "orange"]

# using list()
# myList2 = list(myList1)
# print(myList1)  # ['apple', 'banana', 'cherry', 'orange']
# print(myList2)  # ['apple', 'banana', 'cherry', 'orange']

# using copy()
# myList2 = myList1.copy()
# print(myList1)  # ['apple', 'banana', 'cherry', 'orange']
# print(myList2)  # ['apple', 'banana', 'cherry', 'orange']

# Example 11 : combine/join list

# myList1 = ["apple", "banana", "cherry"]
# myList2 = ["orange", "mango", "melon", "kiwi"]

# using + operator
# myList3 = myList1+myList2
# print(myList3)  # ['apple', 'banana', 'cherry', 'orange', 'mango', 'melon', 'kiwi']

# print(myList1)  # ['apple', 'banana', 'cherry']
# # using loop statement
# for i in myList2:
#     myList1.append(i)
# print(myList1)  # ['apple', 'banana', 'cherry', 'orange', 'mango', 'melon', 'kiwi']

# using extend()
# myList1.extend(myList2)
# print(myList1)  # ['apple', 'banana', 'cherry', 'orange', 'mango', 'melon', 'kiwi']

# Example 11 : compare List
myList1 = ["apple", "banana", "cherry"]
myList2 = ["orange", "mango", "melon", "kiwi"]
myList3 = ["apple", "banana", "cherry"]
if myList1 == myList2:
    print("List are same/equal")
else:
    print("List are not same/not equal")

if myList1 == myList3:
    print("List are same/equal")
else:
    print("List are not same/not equal")





