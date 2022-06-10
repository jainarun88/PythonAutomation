import sys
sys.path.append("C:/Learning/PythonAutomation/Python Basics/ModulesAndPackages/Pack1")
sys.path.append("C:/Learning/PythonAutomation/Python Basics/ModulesAndPackages/Pack1/Pack2")

# Approach 1:
# import Module1
# import Module3
# Module1.display()
# Module3.now()

# Approach 2:
from Module1 import *
from Module3 import *

display()
now()
