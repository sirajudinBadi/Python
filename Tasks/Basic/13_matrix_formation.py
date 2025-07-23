"""
    13. Convert String to matrix having K characters per row Using list comprehension + slicing.
    Input : test_str = ‘GeeksforGeeks is best’, K = 7
    Output : [[‘G’, ‘e’, ‘e’, ‘k’, ‘s’, ‘f’, ‘o’], [‘r’, ‘G’, ‘e’, ‘e’, ‘k’, ‘s’, ‘ ‘], [‘i’, ‘s’, ‘ ‘, ‘b’, ‘e’, ‘s’, ‘t’]]
    Explanation : Each character is assigned to 7 element row in matrix.
"""
# print(len('GeeksforGeeks is best'))
# sentence = "GeeksforGeeks is best"
# matrix = []
# counter = 0
# for i in range(3):
#     row = []
#     for j in range(7):
#         row.append(sentence[counter])
#         counter+=1
#
#     matrix.append(row)

def str_to_matrix(sentence, rows, cols):
    max_len = len(sentence)
    matrix = [list(sentence[i:i+cols]) for i in range(0, max_len, cols)]
    return matrix

print(str_to_matrix("Today is the best day from the perspective of performance...", 10, 6))
