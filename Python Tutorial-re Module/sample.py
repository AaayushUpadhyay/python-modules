import re
from typing import Pattern

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
cat
bat
pat
rat
'''

sentence = 'Start a sentence and then bring it to an end'

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''


# Raw strings are strings prefixed with r
# Using r tell python not to interpret \ in a special way
# print('\tTab')
# print(r'\tTab')

# Using finditer
# Pattern=re.compile(r'abc')
# matches=re.finditer(Pattern,text_to_search)
# for match in matches:
# 	print(match)

# <re.Match object; span=(1, 4), match='abc'>


# Pattern=re.compile(r'coreyms\.com')
# matches=re.finditer(Pattern,text_to_search)
# for match in matches:
# 	print(match)


# Word Boundary - word boundary matlab whitespace, or non alpha-numeric character
# Ha HaHa
# Matching a Ha with a word boundary before it
# Pattern=re.compile(r'\bHa')
# matches=re.finditer(Pattern,text_to_search)
# for match in matches:
# 	print(match)
# <re.Match object; span=(66, 68), match='Ha'>
# <re.Match object; span=(69, 71), match='Ha'>

# Ha not having a word boundary before it 
# Pattern=re.compile(r'\BHa')
# matches=re.finditer(Pattern,text_to_search)
# for match in matches:
# 	print(match)


# Pattern to match phone numbers in text_to_search

# Pattern=re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
# matches=re.finditer(Pattern,text_to_search)
# for match in matches:
# 	print(match)

# Pattern to match phone numbers in data.txt

# with open('data.txt','r') as f:
# 	contents=f.read()
# 	Pattern=re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
# 	matches=re.finditer(Pattern,contents)
# 	for match in matches:
# 		print(match)
		


# Using Character Sets


# Pattern to match phone numbers in text_to_search exactly having . or -
# Pattern=re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
# # [-.] : ya to yeh character - hoga ya .
# matches=re.finditer(Pattern,text_to_search)
# for match in matches:
# 	print(match)


# Pattern to match phone numbers in text_to_search exactly having 800 or 900
# Pattern=re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
# # [-.] : ya to yeh character - hoga ya .
# matches=re.finditer(Pattern,text_to_search)
# for match in matches:
# 	print(match)


 # Pattern to match all three letter words that end in 'at' except 'bat'
# Pattern=re.compile(r'[^b]at')
# matches=re.finditer(Pattern,text_to_search)
# for match in matches:
# 	print(match)


# To match more than more characters at once we use Quantifiers
# Pattern=re.compile(r'\d{3}[.*-]\d{3}[.*-]\d{4}')
# matches=re.finditer(Pattern,text_to_search)
# for match in matches:
# 	print(match)


# Pattern to match names in text_to_search
# Pattern=re.compile(r'M(r|s|rs)\.?\s[A-Z][a-z]*')
# matches=re.finditer(Pattern,text_to_search)
# for match in matches:
# 	print(match)

# Pattern to match emails
# Pattern=re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
# matches=re.finditer(Pattern,emails)
# for match in matches:
# 	print(match)


urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

# Pattern to match urls
# Pattern=re.compile(r'https?://(www\.)?\w*.\w*')
# matches=re.finditer(Pattern,urls)
# for match in matches:
# 	print(match)

# Groupings
# Pattern=re.compile(r'https?://(www\.)?(\w*)(.\w*)')
# matches=re.finditer(Pattern,urls)
# for match in matches:
# 	print(match.group(0),match.group(1),match.group(2),match.group(3))

Pattern=re.compile(r'https?://(www\.)?(\w*)(.\w*)')

# everytime the pattern is matched us pattern ki jagah yeh subbed_urls a jayega

subbed_urls = Pattern.sub(r'\2\3',urls)
print(subbed_urls)