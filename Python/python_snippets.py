# -*- coding: utf-8 -*-

# In[]


# In[]
'''
Check the source code of a python function
'''
import inspect
lines = inspect.getsourcelines(function_name)
print("".join(lines[0]))


# In[]
'''
Stop poping out warning messages
'''
import warnings
warnings.filterwarnings('ignore')


