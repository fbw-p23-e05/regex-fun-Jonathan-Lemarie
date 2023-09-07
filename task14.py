
# - Task 14 -- Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.

import re

#pattern = '\w*[0-9]*_'


# correction pattern below:
# pattern = [a-zA-Z0-9_]+  or 
pattern = '\w+'

sentence =  'Traveling to the beau_tiful Costa Rica.' # does not find
sentence_1 =  'Traveling to the beautiful Czosta Rica.' # find 

print(re.search(pattern, sentence))
print(re.search(pattern, sentence_1))