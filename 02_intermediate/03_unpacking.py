l = [1, 2, 3, 4, 5, 6]
# print(*l)


def print_params(**kwargs):
    for key, val in kwargs.items():
        print(key, val)

d = {"name" : "Siraj", "age" : 34, "email" : "user@example.com"}
# print_params(**d)

d1 = {1 : "One", 2 : "Two"}
d2 = {3 : "Three", 4 : "Four"}
d3 = {5 : "Five", 6 : "Six"}

print({**d1, **d2, **d3})