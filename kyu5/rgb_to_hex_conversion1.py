'''
Heeran Kim
28-Jul-2024

RGB To Hex Conversion
5 kyu

The rgb function is incomplete. Complete it so that passing in RGB
decimal values will result in a hexadecimal representation being returned.
Valid decimal values for RGB are 0 - 255. Any values that fall out
of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long,
the shorthand with 3 will not work here.

Examples (input --> output):
255, 255, 255 --> "FFFFFF"
255, 255, 300 --> "FFFFFF"
0, 0, 0       --> "000000"
148, 0, 211   --> "9400D3"
'''


def rgb(r, g, b):
    rgbs = [r, g, b]
    rgbs_rounded = []
    for e in rgbs:
        e = min(255, e)
        e = max(0, e)
        rgbs_rounded.append(e)

    return "".join([hex(e)[2:] if e >= 16 else '0'+hex(e)[2:] for e in rgbs_rounded]).upper()


print(rgb(148, 0, 211))
print(rgb(0, 0, 0))
print(rgb(-20, 275, 125))
