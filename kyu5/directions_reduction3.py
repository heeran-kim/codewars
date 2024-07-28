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


def dir_reduc(arr):
    dir = " ".join(arr)
    dir2 = dir.replace("NORTH SOUTH", '').replace("SOUTH NORTH",'').replace("EAST WEST",'').replace("WEST EAST",'')
    dir3 = dir2.split()
    return dir_reduc(dir3) if len(dir3) < len(arr) else dir3


print(dir_reduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
