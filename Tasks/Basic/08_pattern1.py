
def print_pattern(n):
    counter = 1
    for i in range(1, n+1):
        start = counter + i -1
        for j in range(start, start-i, -1):
            print(j, end=" ")
            counter+=1
        print()

print_pattern(4)