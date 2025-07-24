
test_list = [3456, 23, 128, 235, 982]
digit_list = [2, 3, 5, 4]

allowed_digits = [str(i) for i in digit_list]
filtered_list = list(filter(lambda x : all(digit in allowed_digits for digit in str(x)), test_list))
print(filtered_list)

