def is_palindrome_num(n):
    str_num = str(n)
    if n == int(str_num[::-1]):
        return "YES it is Palindrome Number."
    else:
        return "NO it is not a Palindrome Number."

try:
    num = int(input("Provide number to check if palindrome or not : "))
except ValueError:
    print("Only Integer is allowed.")
else:
    print(is_palindrome_num(num))