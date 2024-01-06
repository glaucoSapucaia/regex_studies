'''Python RegEx flags and shortcuts

FLAGS
Use | for more than one flags

1. IGNORECASE or I => Ignore upper and lower case letters
2. ASCII or A => Return all characters except ACCENTS

3. MULTILINE or M => Parses the string by lines, not as a whole
4. DOTALL or S => Allows the ' . ' read line breaks

5. VERBOSE or X => Allows comments within the regular expression
SHORTCUTS

3. Accents
    Only PYTHON => escape + w
    Other languages => [À-ú]

    Use escape = W for the inverse return

    Many Meta Characters invert their value with UPPERCASE
    W => [^w]

4. d => Only numbers | D => except numbers
5. s => White spaces and line breaks | S => except spaces and line breaks
6. b => Border of the elements (starts and ends) | B => non-border
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

enter4 = 'a    123.456.789-12     b'

enter5 = '''
953.346.009-02 ABC
123.456.781-18 DEF
423.786.269-11
'''

# IGNORECASE or I example
print(re.findall('SaBe', enter, flags=re.IGNORECASE))
print('_' * 100)

# find all, include accents
print(re.findall(r'[a-zA-Z0-9À-ú]+', enter, flags=re.I))
print('_' * 100)

# only PYTHON
# All characters and accents
print(re.findall(r'[\w]+', enter, flags=re.I))
print('_' * 100)

print(re.findall(r'[\w]+', enter, flags=re.ASCII))
print('_' * 100)

# not characters
print(re.findall(r'[\W]+', enter))

# not characters, but include accents
print(re.findall(r'[\W]+', enter, flags=re.ASCII))
print('_' * 100)

# \d and \D => control numbers
print(re.findall(r'\d', enter4))
print(re.findall(r'\D', enter4))
print('_' * 100)

# \s and \S => spaces and line breaks
print(re.findall(r'\s+', enter))
print(re.findall(r'\S+', enter))
print('_' * 100)

# b => Border of the elements (starts and ends)
print(re.findall(r'\w+emos\b', enter))
print(re.findall(r'\ba\w+', enter, flags=re.I))

# only 4 characters words
print(re.findall(r'\b\w{4}\b', enter, flags=re.I))
print('_' * 100)

# MULTILINE or M => Parses the string by lines, not as a whole
print(re.findall(r'[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}', enter5))

# return nothing
print(re.findall(r'^[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}$', enter5))

# return per line
print(re.findall(
    r'^[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}$', enter5, flags=re.MULTILINE | re.IGNORECASE))
