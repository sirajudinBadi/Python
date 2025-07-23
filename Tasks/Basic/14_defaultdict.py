from collections import defaultdict

"""
14. Join Tuples if similar initial element using defaultdict.
Input  : test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)] 
Output : [(5, 6, 7, 8), (6, 10), (7, 13)] 
"""


def grouped_elements(arr, ):
    grouped = defaultdict(list)
    for t in arr:
        l = list(t)
        first_el = l[0]
        for el in l:
            if el in grouped:
                continue
            grouped[first_el].append(el)
    res = []
    for val in grouped.values():
        res.append(tuple(val))
    return res
test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13), (9,120), (5,89,23,89)]
print(grouped_elements(test_list))