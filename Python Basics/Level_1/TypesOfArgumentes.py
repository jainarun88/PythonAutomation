# Example 1:
# def func(i, j):
#     print(i, j)
#
#
# func(10, 20)  # Positional Arguments
# func(j=20, i=10)  # Keyword Arguments
# func(i=20, j=10)  # Keyword Arguments

# Example 2: default values assign to positional argument
# def func(i, j=10):
#     print(i, j)
#
#
# func(100, 200)  # Positional Arguments  100 200
# func(100)  # Positional Arguments  100 10

# Example 3: default values assign to keyword argument
# def greetings(name, greetMsg):
#     print(greetMsg+" "+name)
#
#
# greetings(name="John", greetMsg="Hello")  # Hello John
# greetings(greetMsg="Hello", name="John")  # Hello John

# Example 4:
# def my_func(a, b, c):
#     print(a, b, c)


# my_func(10, 20, 30)  # Positional Arguments
# my_func(a=10, b=20, c=30)  # Keyword Arguments
# my_func(b=20, a=10, c=30)  # Keyword Arguments
#
# my_func(10, 20, c=30)  # Combination of both positional and keyword arguments
# my_func(10, b=20, c=30)
# # my_func(10, b=20, 30)  # SyntaxError: positional argument follows keyword argument
# my_func(10, 20, b=30)  # TypeError: my_func() got multiple values for argument 'b' (Logical Error)

# Example 5: Function can return multiple values
def largest(a, b):
    if a>b:
        return a, b
    else:
        return b, a


print(largest(100, 200))  # (200, 100)
print(largest(20, 10))  # (20, 10)

res = largest(100, 200)
print(res)
print(type(res))  # tuple

