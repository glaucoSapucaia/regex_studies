import re
from pprint import pprint

emails = '''
abc-@mail.com
abc-d@mail.com
abc..def@mail.com
abc.def@mail.com
.abc@mail.com
abc@mail.com
abc#def@mail.com
abc_def@mail.com
abc.def@mail.c
abc.def@mail.cc
abc.def@mail#archive.com
abc.def@mail-archive.com
abc.def@mail
abc.def@mail.org
abc.def@mail..com
abc.def@mail.com
'''

regex = re.compile(r'^\w+(?:[._\-@]\w+)*\.[a-z]{2,}$', flags=re.MULTILINE)

pprint(regex.findall(emails))
