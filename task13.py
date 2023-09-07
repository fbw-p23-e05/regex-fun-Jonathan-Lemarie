
# -- Task 13 -- Write a Python program that matches a word containing 'z', not the start or end of the word.

import re

#pattern = '[^z]+z+[^z]+?'  # 

#  correction pattern below :  
pattern = '[a-yA-y]+z+[a-yA-Y]+'

sentence =  'zTraveling to the beautiful Costa Rica.' # does not find
sentence_1 =  'Traveling to the beautiful Czzosta Rica.' # find 

print(re.search(pattern, sentence))
print(re.search(pattern, sentence_1))