'''Use unicode characters'''

from random import randint, choice, shuffle
import re


def zeroToNine():
    return chr(randint(48, 57))


def aToz():
    return chr(randint(97, 122))


def AToZ():
    return chr(randint(65, 90))


def strangeChars():
    rand_range = [
        randint(32, 47),
        randint(58, 64),
        randint(91, 96),
        randint(123, 126),
    ]
    return chr(choice(rand_range))


def createPass(
        length=12,
        upper=True,
        lower=True,
        numbers=True,
        chars=True,
):
    password = []

    for i in range(length):
        if upper:
            password.append(AToZ())
        if lower:
            password.append(aToz())
        if numbers:
            password.append(zeroToNine())
        if chars:
            password.append(strangeChars())

    password = password[:length]
    shuffle(password)
    return ''.join(password)


# RegEx with UniCode characters
regex_uni = re.compile(
    r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\u0020-\u002F\u003A-\u0040\u005B-\u0060\u007B-\u007E]).{12,}$",
    flags=re.MULTILINE)

# RegEx with UniCode "REAL" characters
regex_real_chars = re.compile(r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[ -\/:-@[-`{-~]).{12,}",
                              flags=re.MULTILINE)

test_passwords = '''
h8YX{n
176:5V^JA]H;
G6z9a|3YA<d~
vnQBZSj3882u
wPn?rQPZz,]_
;N8F8@M4%0O%
LS^p[[zmI|Zf
gPl4I;
yFM200DoRb6f
Ul=nn#KEI|{q
3t?R7L[sOa~3
lgt;k%B|DBZ|
'''

if __name__ == '__main__':
    print('My strong passwords!')
    for i in range(5):
        print(createPass())
    print()

    print('Without UPPERCASE!')
    for i in range(5):
        print(createPass(upper=False))
    print()

    print('Without LOWERCASE!')
    for i in range(5):
        print(createPass(lower=False))
    print()

    print('Without NUMBERS!')
    for i in range(5):
        print(createPass(numbers=False))
    print()

    print('Without CHARS!')
    for i in range(5):
        print(createPass(chars=False))
    print()

    print('Without CORRECT LENGTH!')
    for i in range(5):
        print(createPass(length=6))
    print()
print('_' * 100)

print(regex_uni.findall(test_passwords))
print('_' * 100)
print(regex_real_chars.findall(test_passwords))
