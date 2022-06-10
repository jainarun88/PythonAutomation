# Example 1:
# class MyOOPsClass:
#     def myFunc(self):
#         pass
#
#     def display(self, name):
#         print(name)
#
#
# mc1 = MyOOPsClass()
# mc1.myFunc()
# mc1.display("scott")

# Example 2:
# class MyClass:
#     def m1(self):
#         print("This is a instance method.....")
#
#     @staticmethod
#     def m2(self, num):
#         print(self, num)
#
#
# mc = MyClass()
# mc.m1()
# mc.m2(10, 20)  # 10 20
#
# MyClass.m2(10, 20)  # 10 20 - here calling static method directly using class name not through object

# Example 3:
# class MyClass:
#     a, b = 10, 20  # Class Variables
#
#     def add(self):
#         print(self.a + self.b)
#
#     def mul(self):
#         print(self.a * self.b)
#
#
# mc = MyClass()
# mc.add()  # 30
# mc.mul()  # 200

# Example 4:
# i, j = 10, 15  # Global Variables
#
#
# class MyClass:
#     a, b = 10, 20  # Class Variables
#
#     def add(self, x, y):
#         print(x + y)  # x, y are local variables
#         print(self.a + self.b)  # a, b are class variables
#         print(i + j)  # i, j are global Variables
#
#
# mc = MyClass()
# mc.add(100, 200)

# Example 5:
# a, b = 15, 25  # Global Variables
#
#
# class MyClass:
#     a, b = 10, 20  # Class Variables
#
#     def add(self, a, b):
#         print(a + b)  # a, b are local variables
#         print(self.a + self.b)  # a, b are class variables
#         print(globals()['a'] + globals()['b'])  # a, b are global Variables
#
#
# mc = MyClass()
# mc.add(100, 200)

# Example 6 : One class can have multiple object
# class MyClass:
#     def display(self, name):
#         print("This is a display method....")
#         print(name)
#
#
# obj1 = MyClass()
# obj1.display("Arun")
#
# obj2 = MyClass()
# obj2.display("Jain")

# Example 7: Constructor example
# class MyClass:
#     def __init__(self):
#         print("This is a Constructor.....")
#     def m1(self):
#         print("This M1 method...")
#     def m2(self, x, y):
#         return x+y
#
#
# mc = MyClass()  # invoke constructor by default
# mc.m1()  # method we have call explicitly by using object
# add = mc.m2(10, 20)
# print(add)  # 30

# Example 8:
# class MyClass:
#     name = "Arun"
#
#     def __init__(self, name):  # Constructor expecting one argument
#         print(name)
#         print(self.name)
#
#
# mc = MyClass("Jain")  # passing parameter to the constructor

# # Example 9:
# # Req: Employee Class
# # Constructor : eid, ename, esal
# # display() : print eid, ename, esal
#
# class Employee:
#     def __init__(self, eid, ename, esal):
#         self.eid = eid
#         self.ename = ename
#         self.esal = esal
#
#     def display(self):
#         print(self.eid, self.ename, self.esal)
#
#
# emp1 = Employee(101, "Arun", 500000)
# emp1.display()  # 101 Arun 500000
#
# emp2 = Employee(102, "Ravi", 700000)
# emp2.display()  # 102 Ravi 700000

# Example 10:
# Req: Employee Class
# Constructor : eid, ename, esal
# display() : print eid, ename, esal

class Employee:
    def __init__(self, eid, ename, esal):
        self.eid = eid
        self.ename = ename
        self.esal = esal

    def __str__(self):
        return self.ename
        # return self.ename, self.eid     #  invalid -  TypeError: __str__ returned non-string (type tuple)


emp1 = Employee(101, "Arun", 500000)
print(emp1)   # Arun

emp2 = Employee(102, "Ravi", 700000)
print(emp2)  # Ravi
