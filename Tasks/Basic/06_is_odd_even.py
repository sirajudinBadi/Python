def odd_even(n):
    if n <= 0:
        return "Please provide valid number"
    if n % 2 == 0:
        return "Number is EVEN."
    else:
        return "Number is ODD"

try:
    number = int(input("Enter number : "))
except ValueError:
    print("Only Integer is allowed.")
else:
    print(odd_even(number))