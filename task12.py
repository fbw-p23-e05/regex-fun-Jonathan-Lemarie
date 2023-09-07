
# -- Task 12 -- Write a Python program that matches a word containing 'z'.

import re

pattern = '\w*z\w*'

sentence =  'Traveling to the beautiful Costa Rica.' # does not find
sentence_1 =  'Traveling to the beautiful Czosta Rica.' # find 

print(re.search(pattern, sentence))
print(re.search(pattern, sentence_1))

