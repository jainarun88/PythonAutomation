# Python Variable Types
# Local Variable
# Declaring a function
def add():
    # Defining local variables. They have scope only within a function
    a = 20
    b = 30
    c = a + b
    print("The sum is:", c)


# Calling a function
add()
# # Accessing local variable outside the function
# print(a)

# Global Variables
# Declare a variable and initialize it
x = 101


# Global variable in function
def mainFunction():
    # printing a global variable
    global x
    print(x)
    # modifying a global variable
    x = "Welcome To Arun's Python World"
    print(x)


mainFunction()
print(x)

# Delete a variable
# Assigning a value to x
y = 6
print(y)
# deleting a variable.
del y
print(y)
