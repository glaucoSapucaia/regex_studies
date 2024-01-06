import re
from pprint import pprint

# valid ipv4

ipv4_1 = '0.0.0.0'
ipv4_2 = '255.255.255.255'

cpf_1 = '123.456.789-01'
cpf_2 = ' 123.456.789-01'
cpf_3 = '12345678901'

# CPF validate

print(re.search(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf_1))  # Match
print(re.search(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf_2))  # None
print(re.search(r'^\d{11}$', cpf_3))  # Match
print('_' * 100)

# IPV validate

ipv4_regex = re.compile(r'''
    ^
    (?:
        25[0-5] | # 250 - 255
        2[0-4][0-9] | # 200 - 249
        1[0-9]{2} | # 100 - 199
        [1-9][0-9] | # 10 - 99       
        [0-9] # 0 - 9          
    )
    \.
    (?:
        25[0-5] | # 250 - 255
        2[0-4][0-9] | # 200 - 249
        1[0-9]{2} | # 100 - 199
        [1-9][0-9] | # 10 - 99       
        [0-9] # 0 - 9          
    )
    \.
    (?:
        25[0-5] | # 250 - 255
        2[0-4][0-9] | # 200 - 249
        1[0-9]{2} | # 100 - 199
        [1-9][0-9] | # 10 - 99       
        [0-9] # 0 - 9          
    )
    \.
    (?:
        25[0-5] | # 250 - 255
        2[0-4][0-9] | # 200 - 249
        1[0-9]{2} | # 100 - 199
        [1-9][0-9] | # 10 - 99       
        [0-9] # 0 - 9          
    )
    $
''', flags=re.VERBOSE)

for i in range(301):
    ipv4 = f'{i}.{i}.{i}.{i}'
    print(ipv4, ipv4_regex.findall(ipv4))
