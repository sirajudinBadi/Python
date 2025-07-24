from collections import Counter

def get_most_common(s):
    d = Counter(s)
    count = 0
    for key,val in d.most_common():
        if count < 3:
            print(key, val)
            count+=1

get_most_common("aabbbccde")