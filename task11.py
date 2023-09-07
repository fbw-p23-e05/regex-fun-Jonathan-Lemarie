
# Task 11 -- Write a Python program that matches a word at the end of a string, with optional punctuation.

import re

#pattern = '\w+.$'   # correct is below
pattern = '\w+[.!?,;]?$'   # or 

sentence =  'Traveling to the beautiful Costa Rica.' # matches
sentence_1 =  'Traveling to the beautiful Costa Rica.!' # does not matches.

print(re.search(pattern, sentence))
print(re.search(pattern, sentence_1))
