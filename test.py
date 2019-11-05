import re

source = 'english_words_01.txt'

with open(source) as f:
    data = f.read()

english_words = re.findall('[a-z]+', data)
ja = re.findall(r'\w+', data)
print(ja)
