# Example 1:
# global_var = 20  # Global Variable
#
#
# def func():
#     local_var = 10  # Local Variable
#     print(local_var)
#     print(global_var)
#
#
# func()
# # print(local_var)  # invalid - local_var is local variable of func()
# print(global_var)  # valid - global_var is global variable

# # Example 2:
# xy = 100  # Global Variable
#
#
# def func():
#     xy = 200  # Local Variable
#     print(xy)
#
#
# print(xy)  # 100
# func()  # 200

# Example 3:
# xy = 100  # Global Variable
#
#
# def func():
#     # global xy = 200  # invalid statement
#     global xy
#     xy = 200  # Local Variable
#     print(xy)
#
#
# print(xy)  # 100
# func()  # 200
# print(xy)  # 200

# Example 4:

def cool():
    global x
    x = 500
    print(x)


# print(x)  # NameError: name 'x' is not defined
cool()
print(x)

