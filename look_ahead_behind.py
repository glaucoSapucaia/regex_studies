'''Lookahead and Lookbehind actions

1. POSITIVE lookahead
    ?=value
2. NEGATIVE lookahead
    ?!value

3. POSITIVE lookbehind
    ?<=value
4. NEGATIVE lookbehind
    ?<!value
'''

import re
from pprint import pprint

logs = '''
ONLINE  192.463.0.1 GHIJK active
OFFLINE  192.463.0.2 GHIJK inactive
OFFLINE  192.463.0.3 GHIJK active
ONLINE  192.463.0.4 GHIJK active
ONLINE  192.463.0.5 GHIJK inactive
OFFLINE  192.463.0.6 GHIJK active
'''

# all IPs
pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', logs))
print('_' * 100)

# IPs more FINAL
pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(\w+)', logs))
print('_' * 100)

# IPs more INITIAL
pprint(re.findall(r'(\w+)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', logs))
print('_' * 100)

# POSITIVE LOOKAHEAD
pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?=active)', logs))

# incative lines
pprint(re.findall(r'(?=.*inactive).+', logs))

# active lines
pprint(re.findall(r'(?=.*[^in]active).+', logs))
print('_' * 100)

# NEGATIVE LOOKAHEAD
pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?!active)', logs))
print('_' * 100)

# POSITIVE LOOKBEHIND
# ONLINE lines
pprint(re.findall(r'\w+(?<=ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', logs))
print('_' * 100)

# NEGATIVE LOOKBEHIND
# OFFLINE lines
pprint(re.findall(r'\w+(?<!ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', logs))
