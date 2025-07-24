from itertools import combinations, permutations


test_list = [3456, 23, 128, 235, 982]
digit_list = [2, 3, 5, 4]

allowed_digits = [str(i) for i in digit_list]
filtered_list = list(filter(lambda x : all(digit in allowed_digits for digit in str(x)), test_list))
print(filtered_list)

# combs = []
# for r in range(1,len(digit_list)+1):
#     combs.extend(combinations(digit_list, r))
# print(combs)
#
# str_test = []
# for num in test_list:
#     num_split = str(num)
#     str_test.append(num_split)
# print(str_test)
# for ls in combs:
#     listed = list(ls)
#     print(listed, end=" ")
