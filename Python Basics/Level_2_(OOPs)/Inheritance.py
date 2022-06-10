# Example 1: Single Inheritance
# class A:
#     def m1(self):
#         print("This is a method of class A....")
#
#
# class B(A):
#     def m2(self):
#         print("This is a method of class B....")
#
#
# objB = B()
# objB.m1()    # This is a method of class A....
# objB.m2()    # This is a method of class B....

# Example 2: Single Inheritance
# class A:
#     x, y = 10, 20
#
#     def m1(self):
#         print(self.x + self.y)
#
#
# class B(A):
#     a, b = 300, 200
#
#     def m2(self):
#         print(self.a - self.b)
#
#
# objB = B()
# objB.m1()   # 30
# objB.m2()   # 100

# # Example 3: Multi level Inheritance
# class A:
#     x, y = 10, 20
#
#     def m1(self):
#         print(self.x + self.y)
#
#
# class B(A):
#     a, b = 300, 200
#
#     def m2(self):
#         print(self.a - self.b)
#
#
# class C(B):
#     i, j = 5, 30
#
#     def m3(self):
#         print(self.i + self.j)
#
#
# objC = C()
# objC.m1()   # 30
# objC.m2()   # 100
# objC.m3()   # 35

# # Example 4: Hierarchy Inheritance
# class A:
#     x, y = 10, 20
#
#     def m1(self):
#         print(self.x + self.y)
#
#
# class B(A):
#     a, b = 300, 200
#
#     def m2(self):
#         print(self.a - self.b)
#
#
# class C(A):
#     i, j = 5, 30
#
#     def m3(self):
#         print(self.i + self.j)
#
#
# objB = B()
# objB.m1()   # 30
# objB.m2()   # 100
#
# objC = C()
# objC.m1()   # 30
# objC.m3()   # 35

# # Example 5: Multiple Inheritance
# class A:
#     x, y = 10, 20
#
#     def m1(self):
#         print(self.x + self.y)
#
#
# class B:
#     a, b = 300, 200
#
#     def m2(self):
#         print(self.a - self.b)
#
#
# class C(A, B):
#     i, j = 5, 30
#
#     def m3(self):
#         print(self.i + self.j)
#
#
# objC = C()
# objC.m1()   # 30
# objC.m2()   # 100
# objC.m3()   # 35

# # Example 6 :
# class A:
#     def m1(self):
#         print("This is m1 method from A class")
#
#
# class B(A):
#     # Override method
#     def m1(self):
#         print("This is m1 method from B class")
#         super().m1()    # Calling(invoking) parent CLASS METHOD into child class using super() keyword
#
#
# objB = B()
# objB.m1()    # This is m1 method from B class

# # Example 7 :
# class A:
#     a, b = 10, 20
#
#
# class B(A):
#     i, j = 100, 200
#
#     # Override method
#     def m(self, x, y):
#         print(x + y)   # local variables  3000
#         print(self.i + self.j)   # class variables  300
#         print(self.a + self.b)   # class variables  30
#
#
# objB = B()
# objB.m(1000, 2000)  # 3000 300 30

# Example 8: overriding variables
# class Parent:
#     name = "Arun"
#
#
# class Child(Parent):
#     name = "Ativeer"
#
#     def test(self):
#         print(super().name)
#
#
# child = Child()
# print(child.name)  # Ativeer
# child.test()   # Arun

# Example 9: overriding methods
# class Bank:
#     def rateOfInterest(self):
#         return 0
#
#
# class XBank(Bank):
#     def rateOfInterest(self):
#         return 10
#
#
# class YBank(Bank):
#     def rateOfInterest(self):
#         return 12
#
#
# objX = XBank()
# print(objX.rateOfInterest()) # 10
#
# objY = YBank()
# print(objY.rateOfInterest())  # 10

# Example 10: overloading methods
# class Human:
#     def sayHello(self, name=None):
#         if name is not None:
#             print("Hello " + name)
#         else:
#             print("Hello")
#
#
# h = Human()
# h.sayHello("Arun")  # Hello Arun
# h.sayHello()   # Hello

# Example 11: overloading
class Calculator:
    def add(self, a=0, b=0, c=0):
        print(a + b + c)


calObj = Calculator()
calObj.add()                # 0
calObj.add(10)              # 10
calObj.add(10, 20)          # 30
calObj.add(10, 20, 30)      # 60
