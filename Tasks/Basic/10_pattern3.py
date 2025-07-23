n = 6
def print_pattern_3(n):
    for i in range(n+1):
        start = 0
        end = i**2 + 1
        step = i*1 if (i*1) != 0 else 1
        for j in range(start, end, step):
            print(j, end=" ")
        print()

try:
    n = int(input("Provide Number of Rows: "))
except ValueError:
    print("Only Integer is allowed.")
else:
    print_pattern_3(n)