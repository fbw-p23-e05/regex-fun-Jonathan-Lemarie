
# Task 4 -- Write a Python program that matches a string that has an a followed by zero or one 'b'.


import re

pattern = 'ab?'   # regex function


# different sentences 
sentence_1 = 'abbbbc'           
sentence_2 = 'hello habibi'
sentence_3 = 'hello aaa0b00'
sentence_4 = 'a0ab'
sentence_5 = 'flying a0'
sentence_6= 'flying ab'
sentence_7 = 'yolo yolo'


print(re.search(pattern, sentence_1)) 
print(re.search(pattern, sentence_2)) 
print(re.search(pattern, sentence_3)) 
print(re.search(pattern, sentence_4)) 
print(re.search(pattern, sentence_5))
print(re.search(pattern, sentence_6))
print(re.search(pattern, sentence_7)) 