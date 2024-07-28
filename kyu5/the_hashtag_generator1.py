"""
Heeran Kim
28-Jul-2024

The Hashtag Generator
5 kyu

Here's the deal:
It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.

Examples
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
"""


def generate_hashtag(s):
    results = "#"
    s = s.strip().split()

    if not s:
        return False

    for word in s:
        if len(word) == 1:
            results += word.upper()
        else:
            results += word[0].upper() + word[1:].lower()

    if len(results) > 140:
        return False

    return results


print(generate_hashtag(" Hello there thanks for trying my Kata"))