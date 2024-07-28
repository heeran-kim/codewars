"""
Heeran Kim
28-Jul-2024

Directions Reduction
5 kyu

Once upon a time, on a way through the old wild mountainous west,…
… a man was given directions to go from one point to another.
The directions were "NORTH", "SOUTH", "WEST", "EAST".
How I crossed a mountainous desert the smart way.

The directions given to the man are, for example, the following (depending on the language):
["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"].

You can immediately see that going "NORTH" and immediately "SOUTH"
is not reasonable, better stay to the same place!
So the task is to give to the man a simplified version of the plan.
A better plan in this case is simply:
["WEST"]
"""


def get_opposite(direction):
    if direction == "NORTH":
        return "SOUTH"
    elif direction == "SOUTH":
        return "NORTH"
    elif direction == "EAST":
        return "WEST"
    elif direction == "WEST":
        return "EAST"


def dir_reduc(arr):
    i = 0
    while True:
        if i >= len(arr)-1:
            break
        if arr[i + 1] == get_opposite(arr[i]):
            arr.pop(i)
            arr.pop(i)
            i = 0
        else:
            i += 1
    return arr


print(dir_reduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
