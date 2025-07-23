def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

try:
    num = int(input("Enter valid number : "))
except ValueError:
    print("Only INTEGERS allowed.")
else:
    print(factorial(num))