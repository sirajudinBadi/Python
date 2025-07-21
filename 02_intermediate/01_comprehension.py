squares = [x**2 for x in range(1, 11)]
# print(squares)

odd_squares = [x**2 for x in range(1,11,2)]
# print(odd_squares)

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

flatten = [item for row in matrix for item in row]
# print(flatten)

transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transpose)

d = {x : x**2 for x in range(1, 11)}
print(d)