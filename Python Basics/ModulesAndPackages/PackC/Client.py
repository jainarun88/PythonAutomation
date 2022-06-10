import sys
sys.path.append("C:/Learning/PythonAutomation/Python Basics/ModulesAndPackages/PackA")
sys.path.append("C:/Learning/PythonAutomation/Python Basics/ModulesAndPackages/PackB")

# Approach 1:
# import Emp
#
# empObj = Emp.Employee(101, "Arun", 500000)
# empObj.displayEmp()
#
# import Stu
#
# stuObj = Stu.Student(1122, "Raj", "A")
# stuObj.displayStu()

# Approach 2:
from Emp import Employee
from Stu import Student
empObj = Employee(101, "Arun", 500000)
empObj.displayEmp()

stuObj = Student(1122, "Raj", "A")
stuObj.displayStu()

