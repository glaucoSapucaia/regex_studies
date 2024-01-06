import re
from pprint import pprint

# valid ipv4

ipv4_1 = '0.0.0.0'
ipv4_2 = '255.255.255.255'

cpf_1 = '123.456.789-01'
cpf_2 = ' 123.456.789-01'
cpf_3 = '12345678901'
cpf_4 = '''
364.574.776-23
487.574.656-45
287.111.111-23
000.001.284-21
288.514.176-11

111.111.111-11
222.222.222-22
333.333.333-33
444.444.444-44
555.555.555-55
'''

# CPF validate

# low validate

print(re.search(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf_1))  # Match
print(re.search(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf_2))  # None
print(re.search(r'^\d{11}$', cpf_3))  # Match
print('_' * 100)

# high validate - non-repeat the same number

cpf_regex = re.compile(
    r"^(?!(\d)\1{2}\.\1{3}\.\1{3}-\1{2})(\d{3}\.\d{3}\.\d{3}-\d{2})$",
    flags=re.MULTILINE)

for cpf in cpf_regex.findall(cpf_4):
    _, cpf = cpf
    print(cpf)
print('_' * 100)

# IPV validate

# long way
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

# short way
ipv4_regex_short = re.compile(
    r'^(?:(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])\.?){4}\b$'
)

for i in range(301):
    ipv4 = f'{i}.{i}.{i}.{i}'
    print(ipv4, ipv4_regex.findall(ipv4))
    print(ipv4, ipv4_regex_short.findall(ipv4))
