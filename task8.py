
# - Task 8 -- Write a Python program to find the sequences of one upper case letter followed by lower case letters.

import re

pattern ='[A-Z][a-z]+'

string = ' The Dog is always Running.'

print(re.findall(pattern, string))

