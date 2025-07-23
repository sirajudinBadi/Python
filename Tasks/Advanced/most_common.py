from collections import Counter

def get_most_common(s):
    d = dict(Counter(s))
    for key, val in d.items():
        print(key, val)

get_most_common("missisippi")