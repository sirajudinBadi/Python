def is_armstrong(n):
    sum = 0
    og_num = n
    num_len = len(str(og_num))
    while n > 0:
        digit = n % 10
        sum += digit ** num_len
        n = n //10

    if sum == og_num:
        return "YES it is ARMSTRONG Number."
    else:
        return "NO it is not ARMSTRONG Number."

try:
    number = int(input("Enter a number : "))
except ValueError:
    print("Only INTEGERS allowed.")
else:
    print(is_armstrong(number))