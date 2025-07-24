def matrix_rotation(data):
    arr = data.strip().splitlines()
    matrix = [list(map(int, line.split())) for line in arr]

    m, n, r = matrix.pop(0)

    layers = []

    # Step 1: Extract each layer
    for layer in range(min(m, n) // 2):
        elements = []

        # top
        for i in range(layer, n - layer):
            elements.append(matrix[layer][i])
        # right
        for i in range(layer + 1, m - 1 - layer):
            elements.append(matrix[i][n - 1 - layer])
        # bottom
        for i in range(n - 1 - layer, layer - 1, -1):
            elements.append(matrix[m - 1 - layer][i])
        # left
        for i in range(m - 2 - layer, layer, -1):
            elements.append(matrix[i][layer])

        layers.append(elements)

    # Step 2: Rotate each layer
    for i in range(len(layers)):
        elements = layers[i]
        rot = r % len(elements)
        layers[i] = elements[rot:] + elements[:rot]

    # Step 3: Put rotated layers back into matrix
    for layer in range(min(m, n) // 2):
        k = 0
        elements = layers[layer]

        # top
        for i in range(layer, n - layer):
            matrix[layer][i] = elements[k]
            k += 1
        # right
        for i in range(layer + 1, m - 1 - layer):
            matrix[i][n - 1 - layer] = elements[k]
            k += 1
        # bottom
        for i in range(n - 1 - layer, layer - 1, -1):
            matrix[m - 1 - layer][i] = elements[k]
            k += 1
        # left
        for i in range(m - 2 - layer, layer, -1):
            matrix[i][layer] = elements[k]
            k += 1

    # Step 4: Print matrix
    for row in matrix:
        for j in row:
            print(str(j), end=" ")
        print()

s = "5 4 7 \n 1 2 3 4 \n 7 8 9 10 \n 13 14 15 16 \n 19 20 21 22 \n 25 26 27 28"
matrix_rotation(s)