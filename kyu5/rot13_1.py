"""
Heeran Kim
28-Jul-2024

Rot13
5 kyu

ROT13 is a simple letter substitution cipher that replaces a letter
with the letter 13 letters after it in the alphabet.
ROT13 is an example of the Caesar cipher.
Create a function that takes a string and returns the string ciphered
with Rot13. If there are numbers or special characters included in the
string, they should be returned as they are. Only letters from the
latin/english alphabet should be shifted, like in the original Rot13
"implementation".

Please note that using encode is considered cheating.
"""

ALPHA = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z']


def rot13(message):
    results = []
    for c in message:
        if c.isalpha() and c.isupper():
            c = c.lower()
            c = ALPHA[(ALPHA.index(c) + 13) % len(ALPHA)].upper()
        elif c.isalpha():
            c = ALPHA[(ALPHA.index(c) + 13) % len(ALPHA)]
        results.append(c)

    return "".join(results)


print(rot13('aA bB zZ 1234 *!?%'))
