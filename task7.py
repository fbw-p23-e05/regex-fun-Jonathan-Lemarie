
#  Task 7 -- Write a Python program to find sequences of lowercase letters joined by an underscore.

import re

pattern = '[a-z]+_[a-z]+'


sentence = 'hello_summer_is_here'
sentence_1 = 'hello summer_is here'

matches = re.findall(pattern, sentence)

#print(re.search(pattern, sentence))


if matches:
    print("Sequences of lowercase letters joined by an underscore found:")
    for match in matches:
        print(match)
else:
    print("No sequences of lowercase letters joined by an underscore found.")

