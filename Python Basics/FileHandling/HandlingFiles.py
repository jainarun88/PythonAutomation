# Example 1: writing the data into text file
# file = open("C:/Learning/PythonAutomation/Python Basics/DemoFiles/myFile.txt", "w")
# file.write("This is my first statement....\n")
# file.write("This is my second statement....\n")
# file.write("This is my third statement....\n")
# file.write("This is my fourth statement....\n")
# file.write("This is my fifth statement....\n")
# file.write("This is my sixth statement....\n")
# file.write("This is my seventh statement....\n")
# file.close()
# print("program completed......")

# Example 2: reading the data from text file
# file = open("C:/Learning/PythonAutomation/Python Basics/DemoFiles/myFile.txt", "r")
# # print(file.read())
# print(file.readline())
# file.close()

# Example 3: appending the data into text file
file = open("C:/Learning/PythonAutomation/Python Basics/DemoFiles/myFile.txt", "a")
file.write("\nThis is my eight statement....\n")
file.write("This is my ninth statement....\n")
file.close()
print("program completed......")




