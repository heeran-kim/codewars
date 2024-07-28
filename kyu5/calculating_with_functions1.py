"""
Heeran Kim
28-Jul-2024

Calculating with Functions
5 kyu

This time we want to write calculations using functions and get the results.

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3

Requirements:
There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical op = ''erations: plus, minus, times, divided_by
Each calculation consist of exactly one op = ''eration and two numbers
The most outer function represents the left op = ''erand, the most inner function represents the right op = ''erand
Division should be integer division. For example, this should return 2, not 2.666666...:
eight(divided_by(three()))
"""


def zero(op=''):
    return eval('0' + op)


def one(op=''):
    return eval('1' + op)


def two(op=''):
    return eval('2' + op)


def three(op=''):
    return eval('3' + op)


def four(op=''):
    return eval('4' + op)


def five(op=''):
    return eval('5' + op)


def six(op=''):
    return eval('6' + op)


def seven(op=''):
    return eval('7' + op)


def eight(op=''):
    return eval('8' + op)


def nine(op=''):
    return eval('9' + op)


def plus(op):
    return '+' + str(op)


def minus(op):
    return '-' + str(op)


def times(op):
    return '*' + str(op)


def divided_by(op):
    return '//' + str(op)


print(seven(times(five())))
print(four(plus(nine())))
print(eight(minus(three())))
print(six(divided_by(two())))
