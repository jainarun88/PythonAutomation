# Set : Unordered (Random), unindex, mutable

# Example 1 : How to create Set
# mySet = {"apple", "banana", "cherry"}
# print(mySet)  # {'cherry', 'apple', 'banana'}

# Example 2 : Accessing item from the Set
# mySet = {"apple", "banana", "cherry"}
# for i in mySet:
#     print(i)

# Example 3 : Check if item is existing in the Set or not
# mySet = {"apple", "banana", "cherry", "orange", "mango", "melon", "kiwi"}
# print("banana" in mySet)  # True
# print("banana2" in mySet)  # False

# Example 4 : Adding item to Set - add(), update()
# mySet = {"apple", "banana", "cherry"}

# add() - add single item
# mySet.add("orange")
# print(mySet)  # {'cherry', 'banana', 'apple', 'orange'}

# update() - add multiple item
# mySet.update(["mango", "kiwi", "orange"])
# print(mySet)  # {'orange', 'cherry', 'mango', 'apple', 'banana', 'kiwi'}

# Example 5 : Set Length
# mySet = {"apple", "banana", "cherry", "orange", "mango", "melon", "kiwi"}
# print(len(mySet))  # 7

# Example 6 : Remove item from the Set - remove(), discard()
# mySet = {"apple", "banana", "cherry"}
# using remove()
# mySet.remove("banana")
# print(mySet)
# mySet.remove("abc")
# print(mySet)  # KeyError: 'abc'

# using discard()
# mySet.discard("apple")
# print(mySet)  # {'cherry', 'banana'}
# mySet.discard("abc")
# print(mySet)  # {'cherry', 'banana'} - will not throw any error

# Example 7 : Clear all item from Set
# mySet = {"apple", "banana", "cherry"}
# mySet.clear()
# print(mySet)  # set()

# del mySet
# print(mySet)   # NameError: name 'mySet' is not defined

# Example 8 : Joining 2 Sets - union()
mySet1 = {"apple", "banana", "cherry"}
mySet2 = {1, 2, 3}
# using union()
# mySet3 = mySet1.union(mySet2)
# print(mySet3)  # {1, 2, 3, 'cherry', 'apple', 'banana'}

# using update()
mySet1.update(mySet2)
print(mySet1)  # {'banana', 1, 2, 3, 'apple', 'cherry'}
