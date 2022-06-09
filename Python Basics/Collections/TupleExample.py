# Tuple - Ordered,  unchangeable, mutable, represents ()

# Example 1 : How to create Tuple
# myTuple = ("apple", "banana", "cherry")
# print(myTuple)
# myTuple1 = ()  # empty tuple

# Example 2 : Accessing item from the Tuple
# myTuple = ("apple", "banana", "cherry")
# print(myTuple[1])  # banana
# print(myTuple[-1])  # cherry

# Example 3 : Range of indexes
# myTuple = ("apple", "banana", "cherry", "orange", "mango", "melon", "kiwi")
# print(myTuple[2:5])  # ('cherry', 'orange', 'mango')
# print(myTuple[:5])  # ('apple', 'banana', 'cherry', 'orange', 'mango')
# print(myTuple[-4:-1])  # ('orange', 'mango', 'melon')

# Example 4 : Change item value from the Tuple
# By default tuple does not allow to change the value bcoz it is immutable, but there is work around
# tuple --> list(modify) --> tuple

# myTuple = ("apple", "banana", "cherry")
# print(myTuple)
# myTuple[0] = "orange"  # TypeError: 'tuple' object does not support item assignment
# print(myTuple)

# myList = list(myTuple)
# myList[0] = "orange"
# myTuple = tuple(myList)
# print(myTuple)  # ('orange', 'banana', 'cherry')

# Example 5 : Read the Tuple item using loop
# myTuple = ("apple", "banana", "cherry", "orange", "mango", "melon", "kiwi")
# for i in myTuple:
#     print(i)

# Example 6 : Check if item is existing in the Tuple or not
# myTuple = ("apple", "banana", "cherry", "orange", "mango", "melon", "kiwi")
# if "apple" in myTuple:
#     print("Yes.. apple is present")
# else:
#     print("No.. apple is not present")

# Example 7 : Tuple length
# myTuple = ("apple", "banana", "cherry", "orange", "mango", "melon", "kiwi")
# tupLen = len(myTuple)
# print(tupLen)  # 7

# Example 8 : Add item in the Tuple
# not possible in tuple due to immutable in the nature
# myTuple = ("apple", "banana", "cherry")
# myTuple[0] = "kiwi"
# print(myTuple)  # TypeError: 'tuple' object does not support item assignment

# Example 9 : Copy Tuple from other Tuple
# myTuple1 = ("apple", "banana", "cherry", "orange")
# myTuple2 = myTuple1
# print(myTuple2)  # ('apple', 'banana', 'cherry', 'orange')

# Example 10 : Remove item from Tuple - not possible due to immutable in nature
# myTuple1 = ("apple", "banana", "cherry", "orange")
# myTuple1.remove("apple")  # invalid statement

# del myTuple1
# print(myTuple1)  # NameError: name 'myTuple1' is not defined

# Example 11 : combine/join Tuple
# myTuple1 = ("apple", "banana", "cherry")
# myTuple2 = ("orange", "mango", "melon", "kiwi")
# myTuple3 = myTuple1+myTuple2
# print(myTuple3)  # ('apple', 'banana', 'cherry', 'orange', 'mango', 'melon', 'kiwi')

# Example 11 : compare Tuple
myTuple1 = ("apple", "banana", "cherry")
myTuple2 = ("orange", "mango", "melon", "kiwi")
myTuple3 = ("apple", "banana", "cherry")
if myTuple1 == myTuple2:
    print("Tuples are same/equal")
else:
    print("Tuples are not same/not equal")

if myTuple1 == myTuple3:
    print("Tuples are same/equal")
else:
    print("Tuples are not same/not equal")
