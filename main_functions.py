import re

enter = 'Esse é um teste para expressões teste regulares'

print(re.search(r'teste', enter))
print(re.findall(r'teste', enter))
print(re.sub(r'teste', 'ABC', enter))
print(re.sub(r'teste', 'ABC', enter, count=1))

regexp = re.compile(r'teste')

print('_' * 100)
print(regexp.search(enter))
print(regexp.findall(enter))
print(regexp.sub('DEF', enter))
print(regexp.sub('DEF', enter, count=1))
