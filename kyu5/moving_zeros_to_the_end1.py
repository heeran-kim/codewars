'''
Heeran Kim
28-Jul-2024

Create Phone Number
5 kyu

Write an algorithm that takes an array and moves all of the zeros
to the end,preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
'''


def move_zeros(lst):
    nonzeros = []
    zeros = []
    for n in lst:
        zeros.append(n) if n == 0 else nonzeros.append(n)
    return nonzeros + zeros


print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
