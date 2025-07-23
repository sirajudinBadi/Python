from itertools import product, groupby
from collections import Counter
# print(list(product([1,2,3], repeat=3)))
# s = "missisippi"
# d = Counter(s)
# d = groupby(s)
# print(d)

# for key, group in groupby(sorted(s)):
    # print(key, len(list(group)))

import re

from numpy.ma.extras import unique

s = """
7890
890834
29384756
8975437543
8538789522
9874563215
7845654523
1234567895
4567891236
userAdmin@gmail.com
exampleUser@gmail.com
user-admin@email.com
muliple.user@ad-min.com
"""
# pattern = re.compile(r"[789]\d{9}")
# matches = pattern.finditer(s)
# for match in matches:
#     print(match)

# print(re.split(r"[;,/]", "a,s.df/g;sdf'sdaf/asdf"))
# print(re.sub(r"\d", "#", "hkhjsao894hjkasfd9054jk"))

# print(re.findall(r"[\w\.-]+@[\w\.-]+\.\w{2,}", s))

def is_prime(n):
    if n < 2:
        print("Please enter valid number")

    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
# print(is_prime(15))

def runner_up(n, arr):
    return sorted(set(arr))[-2]
n = 5
arr = [120,108,115,135,145]
# print(runner_up(n, arr))

def find_missing_num(arr):
    n = len(arr)+1
    expected_sum = n* (n+1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum
    
    # max_num = max(arr)
    # arr_sum = sum(arr)
    # actual_sum = 0
    # for i in range(1,max_num+1):
    #     actual_sum+=i
    # return actual_sum-arr_sum

print(find_missing_num([1, 2, 3, 5, 6, 7, 8]))

