
# --    Task 1 --  Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).

import re

pattern = '^[a-zA-Z_0-9]+$'
pattern_1 = '^[a-zA-Z_0-9\s]+$'   # found \s to treat spaces


sentence = 'Hellosunshinetodayitis27degreesoutside'
sentence_1 = 'Hello sunshine today it is 27 degrees outside'
sentence_2 = 'Hello sunshine, today it is 27+ degrees outside.'



print (re.search(pattern , sentence))
#IP = 101.188.67.134

if re.match(pattern, sentence):
    print('the sentence only contain alpha numeric characters')
else:
    print('the sentence does not contains only alpha numeric characters but other signs ')



if re.match(pattern_1, sentence):
    print('the sentence only contain alpha numeric characters')
else:
    print('the sentence does not contains only alpha numeric characters but other signs ')


if re.match(pattern, sentence_1):
    print('the sentence only contain alpha numeric characters')
else:
    print('the sentence does not contains only alpha numeric characters but other signs ')


if re.match(pattern_1, sentence_1):
    print('the sentence only contain alpha numeric characters')
else:
    print('the sentence does not contains only alpha numeric characters but other signs ')


# several examples to get an idea, with the space character and adding signs to the original sentence (sentence_1)
