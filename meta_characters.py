'''RegEx Meta Characters

1. | => or
2. . => Any character, EXCEPT line break
3. [] => Character SET
4. - => range
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
