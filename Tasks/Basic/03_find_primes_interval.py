
def is_prime(n):
    if n <= 1:
        print("Please enter valid number")
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def primes_in_interval(start, end):
    for i in range(start, end+1):
        if is_prime(i):
            print(i, end=" ")

try:
    start = int(input("Provide start point: "))
    end = int(input("Provide end point : "))
except ValueError:
    print("Only Integers are allowed.")
else:
    primes_in_interval(start,end)