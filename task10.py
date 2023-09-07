
# - Task 10 -- Write a Python program that matches a word at the beginning of a string.

import re

pattern = '^\w+'

sentence =  'Traveling to the beautiful Costa Rica.'

print(re.search(pattern, sentence))

