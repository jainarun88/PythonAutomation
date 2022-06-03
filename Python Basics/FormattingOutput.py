# name = "John"
# age = 30
# sal = 50000.50

name, age, sal = "John", 30, 50000.50

# Approach 1
# print(name)
# print(age)
# print(sal)
print(name, age, sal)
print("##########################")

# Approach 2
# Name is : John
# Age is : 30
# Salary is : 50000.5
print("Name is :", name)
print("Age is :", age)
print("Salary is :", sal)
print("##########################")

# Approach 3
print("Name is : %s Age is : %d Salary is : %g" % (name, age, sal))
print("##########################")

# Approach 4 {}
print("Name is : {} Age is : {} Salary is : {}" .format(name, age, sal))
print("Age is : {} Name is : {} Salary is : {}" .format(age, name, sal))
