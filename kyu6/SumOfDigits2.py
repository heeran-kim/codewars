# Heeran Kim
# 28-Jul-2024

'''
Sum of Digits / Digital Root
6 kyu

Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit,
continue reducing in this way until a single-digit number is produced.
The input will be a non-negative integer.
'''


def digital_root(n):
    while n >= 10:
        total = sum(map(int, str(n)))
        n = total
    return n


print(digital_root(16))
print(digital_root(942))