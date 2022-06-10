# Example 1:
# print("This is starting point of program.......")
# print("This is starting point of program.......")
# print("This is starting point of program.......")
# try:
#     print(x)
# except:
#     print("Exception Occurred")
# print("This is ending point of program.......")
# print("This is ending point of program.......")
# print("This is ending point of program.......")

# Example 2:
# print("This is starting point of program.......")
# print("Program in progress")
# try:
#     print(10/0)     # ZeroDivisionError: division by zero
# except ZeroDivisionError:
#     print("Exception occurred .....and handled")
# print("Program Completed")

# Example 3: Multiple Except Blocks - try, except, else, finally
# try:
#     num1, num2 = 10, 5
#     result = num1/num2
#     print("Result is :", result)
# except ZeroDivisionError:
#     print("Thrown ZeroDivisionError Exception......")
# except SyntaxError:
#     print("Thrown SyntaxError Exception......")
# except:
#     print("Exception handled....")
# else:
#     print("No exception occurred...")
# finally:
#     print("Always execute.....")

# Example 4: Raising our own exceptions
def enterAge(num):
    if num < 0:
        raise ValueError("Only Integers are allowed")
    if num % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")


print("Checking number is even or odd by calling function....")
num = int(input("Enter the number : "))
try:
    enterAge(num)
except ValueError:
    print("Value error exception occurred and handled.....")
print("Program Completed......")
