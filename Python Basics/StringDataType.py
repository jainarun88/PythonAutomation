# Create string variable

# Example 1 - ways of creating string variable
# str1 = "welcome"
# str2 = 'welcome'
# str3 = str("welcome")
# str4 = str('welcome')

# creating empty string variables
# name1 = ""
# name2 = ''
# name3 = str()

# Example 2 : ways of creating string variables
# mutable - cannot change the value of the variable
# immutable - can change the value of the variable
# string is immutable
# if the value is changed after update then it is immutable

# str5 = "welcome"
# print(id(str5))
#
# str5 = str5 + " to python"
# print(id(str5))

# Example 3 : + and * with string
# str1 = "welcome"
# print(str1+" programming")  # Concatenation/joining
#
# print(str1*3) # welcomewelcomewelcome

# Example 4 : Slicing [] operator
# Starting index - 0
# Ending index - 1
# str1 = "welcome"
# print(str1[1:3])  # el
# print(str1[:6])  # welcom
# print(str1[2:])  # lcome
#
# print(str1[1:-1])  # elcom
# print(str1[1:-2])  # elco

# Example 5 : ord() and chr()
# print(ord('B'))  # 66 - ASCII code of character
# print(chr(65))  # A -  character represented by ASCII number

# Example 6 : max()   min()    len()
# str1 = "welcome"
# print(min(str1))  # c
# print(max(str1))  # w
# print(len(str1))  # 7

# Example 7 : in,   not in operators - returns true/false
# str1 = "welcome"
# print("come" in str1)  # true
# print("lome" in str1)  # false
#
# print("come" not in str1)  # false
# print("lome" not in str1)  # true

# Example 8 : String Comparison
# print("tim" == "tie")  # false
# print("free" != "freedom")  # true
# print("arrow" > "aron")  # true
# print("right" >= "left")  # true
# print("teeth" < "tee")  # false
# print("yellow" <= "fellow")  # false
# print("abc" > "")  # true

# Example 9 : Testing string True/False
# str1 = "welcome to python"
# print(str1.isalnum())  # False
# print("welcome".isalpha())  # True
# print("2022".isdigit())  # True
# print("first number".isidentifier())  # False
# print(str1.islower())  # True
# print("WELCOME".isupper())  # True
# print(str1.isspace())  # False
# print(" ".isspace())  # True

# Example 10 : Searching for sub-string
# str1 = "welcome to python"
# print(str1.endswith("thon"))  # True
# print(str1.startswith("arun"))  # False
# print(str1.find("come"))  # 3 (position)
# print(str1.find("become"))  # -1 - not found
# print(str1.count("o"))  # 3  - returns  number os occurrences of substring the string

# Example 11 : Converting Strings
# s = "String in PYTHON"
# s1 = s.capitalize()
# print(s1)  # String in python
#
# s2 = s.title()
# print(s2)  # String In Python
#
# s3 = s.lower()
# print(s3)  # string in python
#
# s4 = s.upper()
# print(s4)  # STRING IN PYTHON
#
# s5 = s.swapcase()
# print(s5)  # sTRING IN python
#
# s6 = s.replace("in", "on")
# print(s6)  # Strong on PYTHON

# Example 12 : Reverse a String
# Method1
# str1 = "welcome to python"
# rev_str = ""
# for i in str1:
#     rev_str = i + rev_str
# print(rev_str)

# Method2
# str1 = "welcome to python"
# rev_str = str1[::-1]
# print(rev_str)



