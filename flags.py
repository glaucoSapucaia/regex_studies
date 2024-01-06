'''Python RegEx flags

1. IGNORECASE or I => Ignore upper and lower case letters
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

# IGNORECASE or I example
print(re.findall('SaBe', enter, flags=re.IGNORECASE))
