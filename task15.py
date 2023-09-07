
# Task 15 -- Write a Python program that starts each string with a specific number.


import re

pattern = '^7'



sentence =  '1Traveling to the beautiful Costa Rica.' # does not find
sentence_1 =  'Traveling to the beautiful Czosta Rica.' # find 

string = pattern + sentence

print(string)
print(re.search(pattern, sentence))
print(re.search(pattern, sentence_1))