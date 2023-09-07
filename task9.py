
# task 9 -- Write a Python program that matches a string that has an 'a' followed by anything ending in 'b'.

import re

pattern = '(a.+)b$'   # regex function


# different sentences 
sentence_1 = 'Traveling to the beautiful Costa Rica sounds b'           


print(re.search(pattern, sentence_1)) 

print(re.match(pattern, sentence_1))

print(re.findall(pattern, sentence_1))


# will need to find for those tasks how to put all those string sentences into one list and in a for loop print if it matches or not.

# correction :
# possible pattern could be '[a-zA-Z]*(a.+)b$'     or   '\w*(a.+)b$