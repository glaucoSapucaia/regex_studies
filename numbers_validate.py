import re

number = '''
1
10
+20
-30
10.00
-647363.19202
.10
.2
+20.
.-3
.+7
-47.
2a
B8
'''

regex = re.compile(r'^[+-]?\d+(?:\.\d+)?$', re.MULTILINE)
print(regex.findall(number))
