def fibbonacci_sequence(n):
    a, b = 0, 1
    print("Fibbonacci series : ", end=" ")
    for i in range(n):
        print(a, end=" ")
        a,b = b, a+b

try:
    n = int(input("Enter the number of elements to print: "))
except ValueError:
    print("Only Integers allowed.")
else:
    fibbonacci_sequence(n)