from itertools import compress

"""
12. Extract tuples having K digit elements using map function
Input : test_list = [(54, 2), (34, 55), (222, 23), (12, 45), (78, )], K = 2
Output : [(34, 55), (12, 45), (78,)]
"""
def map_list(arr, k):
    # result = []
    # for t in arr:
    #     bool_val = []
    #     for num in t:
    #         num_str = str(num)
    #         if len(num_str) == k:
    #             bool_val.append(1)
    #         else:
    #             bool_val.append(0)
    #     if sum(bool_val) == len(t):
    #         result.append(t)
    result = list(map(lambda t:all(len(str(num)) == k for num in t), arr))
    return list(compress(arr, result))

print(map_list([(54, 2), (34, 55), (222, 23),(86, 89),(5, 89), (12, 45),(7,8), (78, ), (897, 654)], 2))

