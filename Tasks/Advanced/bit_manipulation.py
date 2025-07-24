
def find_unique(data):
    data = data.strip().split()
    data.pop(0)
    test_arr = [int(i) for i in data]
    unique_el = data[0]
    for el in set(test_arr):
        if test_arr.count(el) < 2:
            unique_el = el
    return unique_el


s = "7 \n 1 3 15 16 3 1 16"
print(find_unique(s))


