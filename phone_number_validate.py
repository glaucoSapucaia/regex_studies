import re
from pprint import pprint

phone_numbers = '''
(21) 9 8873-2566
(11) 7765-8882
(11) 9 8213-2311
(31) 1144-1241
9 6577-8887
1673-1222
'''

phone_number_regex = re.compile(
    r'^(\(\d{2}\)\s9\s(\d{4})-\d{4})$', flags=re.MULTILINE)

for pn in phone_number_regex.findall(phone_numbers):
    phone_number, _ = pn
    print(phone_number)
print('_' * 100)
