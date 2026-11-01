
import re  # The Python "re" module provides regular expression support.

# Why do we use r in Regex?
# 1. What is r?
# r means Raw String in Python.

# It tells Python to treat backslashes (\) as literal characters instead of interpreting them as escape sequences.
# Because Regex uses many backslash patterns, such as:
# - \w – word character
# - \d – digit
# - \s – whitespace
# - \b – word boundary
# Using r makes Regex patterns easier to write.
# 2. What is \w?
# \w matches a single word character.

# It matches:
# - A to Z
# - a to z
# - 0 to 9
# - Underscore _ 

str =  'an example word:cat!!'
match = re.search(r'word:\w\w\w', str)  #r  designates a python 'raw' string
if match:
    print('found')
else:
    print('did not find')  

## Search for pattern 'iii' in string 'piiig'.
# All of the pattern must match, but it may appear anywhere.
## On success, match.group() is matched text.
match = re.search(r'iii', 'piiig') # found, match.group() == "iii"
match = re.search(r'igs', 'piiig') # not found, match == None

## . = any char but \n
match = re.search(r'..g', 'piiig') # found, match.group() == "iig"

## \d = digit char, \w = word char
match = re.search(r'\d\d\d', 'p123g') # found, match.group() == "123"
match = re.search(r'\w\w\w', '@@abcd!!') # found, match.group() == "abc"    


     