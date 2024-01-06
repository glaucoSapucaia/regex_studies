'''RegEx Meta Characters

1. | => or
2. . => Any character, EXCEPT line break
3. [] => Character SET
4. - => Range

# qunatitative meta characters
5. + => One or several characters
6. * => Zero or several characters
7. {} => Zero, many or the exact occurrence
    {, 10} => Zero or 10
    {2, 6} => Range(2, 6)
    {9} => Exact 9 occurrences

8. backslash => Escape character 
9. ? => non-greedy behavior and Range(0, 1)

10. () => Define a group
    Is saved in memory and can be reused => \1, \2, \3, ... (rear view)
    Count rear views by opening parentheses =? 1( 2()) 3()
    To not save and not return the group use => ?:

    ONLY in PYTHON
    Name a group => (?P<name>)
    Use a name group => (?P=name)
'''

import re

enter = """
Quem sabe um dia
Quem sabe um seremos
Quem sabe um viveremos
Quem sabe um morreremos!

Quem é que
Quem é macho
Quem é fêmea
Quem é humano, apenas!

Sabe amar
Sabe de mim e de si
Sabe de nós
Sabe ser um!

Um dia
Um mês
Um ano
Um(a) vida!Sentir primeiro, pensar depois
Perdoar primeiro, julgar depois

Amar primeiro, educar depois
Esquecer primeiro, aprender depois

Libertar primeiro, ensinar depois
Alimentar primeiro, cantar depois

Possuir primeiro, contemplar depois
Agir primeiro, julgar depois

Navegar primeiro, aportar depois
Viver primeiro, morrer depois.
"""

enter2 = """
<p>Lorem1</p> <p>Lorrrem2</p> <p>Lo</p> <div></div>
"""

enter3 = '123.456.789-12'

# | => or example
print(re.findall(r'Quem|Sabe|primeiro', enter))
print('_' * 100)

# . => Any character example
print(re.findall(r'.abe', enter))
print('_' * 100)

# [] => character SET example
print(re.findall(r'[Ss]abe', enter))
print('_' * 100)

# - => range example
print(re.findall(r'[a-zA-Z0-9]m', enter))
print('_' * 100)

# + => One or several characters
print(re.findall(r'r+e', enter))
print(re.sub(r'r+e', 'ABC', enter))
print('_' * 100)

# * => Zero or several characters
print(re.sub(r'r*e', 'DEF', enter))
print('_' * 100)

# {} => Zero, many or the exact occurrence
#     {, 10} => Zero or 10
#     {2, 6} => Range(2, 6)
#     {9} => Exact 9 occurrences
print(re.findall(r'Pos{1,}uir', enter))
print(re.findall(r'Pos{,2}uir', enter))
print(re.findall(r'Pos{2}uir', enter))
print('_' * 100)

# more complex examples
# Greedy and non-greedy (lazy)
# backslash => escape character "\"
print(re.findall(r'<[dipv]{1,3}>.*<\/[dipv]{1,3}>', enter2))
print('_' * 100)

# non-greedy behavior => ?
print(re.findall(r'<[dipv]{1,3}>.*?<\/[dipv]{1,3}>', enter2))
print('_' * 100)

# () => Define a group
#     Is saved in memory and can be reused => 1, 2, 3, ...
print(re.findall(r'<([dipv]{1,3})>.*?<\/\1>', enter2))
print(re.findall(r'(<([dipv]{1,3})>.*?<\/\2>)', enter2))
tags = re.findall(r'(<([dipv]{1,3})>.*?<\/\2>)', enter2)
print()
for tag in tags:
    a, b = tag
    print(a)
tags2 = re.findall(r'(<([dipv]{1,3})>(.*?)<\/\2>)', enter2)
print()
for tag in tags2:
    a, b, c = tag
    print(c)
print()

# not save and not return an group => ?:
print(re.findall(r'<([dipv]{1,3})>(?:.*?)<\/\1>', enter2))
print('_' * 100)

# more examples
print(re.findall(r'[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}', enter3))
print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', enter3))
print(re.findall(r'[0-9]{3}\.|[0-9]{3}-|[0-9]{2}', enter3))
print('_' * 100)

# group with name
print(re.findall(
    r'<(?P<my_group>[dipv]{1,3})>(?:.*?)<\/(?P=my_group)>', enter2))
print('_' * 100)

# sub with groups
print(re.sub(r'(<(.+?)>)(.*?)(<\/\2>)', r'\1ABC\4', enter2))
