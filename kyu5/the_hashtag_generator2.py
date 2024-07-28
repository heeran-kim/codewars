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
    for word in s.split():
        results += word.capitalize()

    return False if (len(s) == 0 or len(results) > 140) else results


print(generate_hashtag(" Hello there thanks for trying my Kata"))