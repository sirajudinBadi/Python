from collections import Counter

def word_order(s):
    list_of_str = s.strip().splitlines()
    words = list_of_str[1:]
    d = dict(Counter(words))
    print(len(d.values()))
    for val in d.values():
        print(val, end=" ")


input_str = """
4
bcdef
abcdefg
bcde
bcdef
"""

word_order(input_str)