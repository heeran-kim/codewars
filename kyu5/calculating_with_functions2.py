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


def identify(x): return x


def zero(f=identify): return f(0)
def one(f=identify): return f(1)
def two(f=identify): return f(2)
def three(f=identify): return f(3)
def four(f=identify): return f(4)
def five(f=identify): return f(5)
def six(f=identify): return f(6)
def seven(f=identify): return f(7)
def eight(f=identify): return f(8)
def nine(f=identify): return f(9)


def plus(a): return lambda x: x + a
def minus(a): return lambda x: x - a
def times(a): return lambda x: x * a
def divided_by(a): return lambda x: x // a


print(seven(times(five())))
print(four(plus(nine())))
print(eight(minus(three())))
print(six(divided_by(two())))
