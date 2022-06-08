# Conditional Statements
#  if if..else  elif

# Example1 : Print a person is eligible for vote or not
# age >=18

# age = int(input("Enter Person's age : "))
# if age >= 18:
#     print("Eligible for vote")
# else:
#     print("Not eligible for vote")

# Example 2

# if True:
#     print("True Condition")
# else:
#     print("False Condition")

# Example 3
# if 0:
#     print("One")
# else:
#     print("Zero")

# Example 4 : Find a number is even/ood num%2=0
# num = int(input("Enter Number : "))
# if num % 2 == 0:
#     print("Given number is Even")
# else:
#     print("Given number is Odd")

# Example 5 : if else in single line (ternary operator)
# num = int(input("Enter Number : "))
# print("Even number") if num % 2 == 0 else print("Odd number")

# Example 6 : if else - multiple statement in single line
# num = int(input("Enter Number : "))
# {print("hello"), print("Python")} if num >= 10 else {print("hi"), print("Java")}

# # Example 7 : Multiple condition using - elif
# weekNo = int(input("Enter Week Number : "))
# if weekNo == 1:
#     print("Sunday")
# elif weekNo == 2:
#     print("Monday")
# elif weekNo == 3:
#     print("Tuesday")
# elif weekNo == 4:
#     print("Wednesday")
# elif weekNo == 5:
#     print("Thursday")
# elif weekNo == 6:
#     print("Friday")
# elif weekNo == 7:
#     print("Saturday")
# else:
#     print("Invalid week number")

# Assignment 1 : Print week number if provide week-name as input
# weekName = input("Enter Week Name : ")
# if weekName == "Sunday":
#     print("Week Day : 1")
# elif weekName == "Monday":
#     print("Week Day : 2")
# elif weekName == "Tuesday":
#     print("Week Day : 3")
# elif weekName == "Wednesday":
#     print("Week Day : 4")
# elif weekName == "Thursday":
#     print("Week Day : 5")
# elif weekName == "Friday":
#     print("Week Day : 6")
# elif weekName == "Saturday":
#     print("Week Day : 7")
# else:
#     print("Invalid week name")

# Assignment 2 - Check the given number is Positive or Negative
# num = int(input("Enter the number : "))
# if num >= 0:
#     print("Number is Positive")
# else:
#     print("Number is Negative")

# Assignment 3 - Check the largest of 2 numbers
# num1 = int(input("Enter First Number : "))
# num2 = int(input("Enter Second Number : "))
# if num1 > num2:
#     print(str(num1) + " (first number) is greater then " + str(num2) + " (second number)")
# else:
#     print(str(num2) + " (second number) is greater then " + str(num1) + "(first number)")

# Assignment 4 - Check the largest of 3 numbers
num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))
num3 = int(input("Enter Third Number : "))
if num1 > num2 and num1 > num3:
    print(str(num1) + " (first number) is greater then " + str(num2) + " (second number), and " + str(num3) + "(third "
                                                                                                              "number)")
elif num2 > num1 and num2 > num3:
    print(str(num2) + " (second number) is greater then " + str(num1) + " (first number), and " + str(num3) + "(third "
                                                                                                              "number)")
elif num3 > num1 and num3 > num2:
    print(str(num3) + " (third number) is greater then " + str(num1) + " (first number), and " + str(num2) + "(second "
                                                                                                             "number)")
else:
    print("Invalid Combination")
