def matrix_rotation(data):
    raw_data = data.strip().splitlines()
    matrix = [list(map(int, el.split())) for el in raw_data]
    rows, cols, r = matrix.pop(0)

    layers = []
    for layer in range(min(rows, cols)//2):
        elements = []

        # Top
        for i in range(layer, cols-layer):
            elements.append(matrix[layer][i])

        # Right
        for i in range(layer+1, rows-layer-1):
            elements.append(matrix[i][cols-1-layer])

        # Bottom
        for i in range(cols-1-layer, layer-1, -1):
            elements.append(matrix[rows-layer-1][i])

        # Left
        for i in range(rows-layer-2, layer, -1):
            elements.append(matrix[i][layer])
        layers.append(elements)

    for i in range(len(layers)):
        elements = layers[i]
        rotations = r % len(elements)
        layers[i] = elements[rotations:] + elements[:rotations]

    for layer in range(min(rows, cols)//2):
        k = 0
        elements = layers[layer]

        # top
        for i in range(layer, cols - layer):
            matrix[layer][i] = elements[k]
            k += 1

        # Right
        for i in range(layer+1, rows-1-layer):
            matrix[i][cols-layer-1] = elements[k]
            k+=1

        # Bottom
        for i in range(cols-layer-1, layer-1, -1):
            matrix[rows-1-layer][i] = elements[k]
            k+=1

        # Left
        for i in range(rows-layer-2, layer, -1):
            matrix[i][layer] = elements[k]
            k+=1

    for row in matrix:
        for j in row:
            print(str(j), end=" ")
        print()


s = "4 4 1 \n 1 2 3 4 \n 5 6 7 8 \n 9 10 11 12 \n 13 14 15 16"
matrix_rotation(s)