# for i in range(10):
#     print(i,i+1, sep=",", end=" | ")
# print()

# input = input("Type the numbers").split(" ")
# print(input, type(input))

# input = list(map(int, input("Type the list of numbers : ").split()))
# print(input)

# ------------------------------------------------------ MAP --------------------------------------------

# # Convert list of string into integer
# s = ["1", "2", "3", "4", "5"]
# int_list = list(map(int, s))
# print(int_list)


# # Convert each word of list to uppercase
# words_lower = ['python', 'map', 'function']
# words_upper = list(map(lambda word : word.upper(), words_lower))
# print(words_upper)

# # Find the length of each word in list
# l = ['hello', 'world', 'map']
# char_count = list(map(lambda x : len(x), l))
# print(char_count)

# # Percentage string to Float
# percentage_li = ['90%', '85%', '100%']
# map_float_li = list(map(lambda x : float(x.removesuffix("%")), percentage_li))
# print(map_float_li)

# ------------------------------------------------------------ FILTER --------------------------------------------
l = ['madam', 'apple', 'noon']
palindrome = list(filter(lambda x : x == x[::-1], l))
print(palindrome)

words = ['HELLO', 'World', 'PYTHON', 'java']
uppercase = list(filter(lambda x : x.isupper(), words))
# print(uppercase)

vals = [0, 1, '', 'hello', [], [1]] 
truthy = list(filter(lambda x : bool(x), vals))
# print(truthy)

