# try:
#     input_num = int(input("Enter the number : "))
#     a = 234 / input_num
#     print(a)
# except ValueError as e :
#     print(f"Please input valid value.")
# except ZeroDivisionError :
#     print("Can not divide number by Zero.")
# else :
#     print("Good to go...")
# finally:
#     print("End of programme.")

class CustomError(Exception):
    pass

try:
    n = int(input("Provide input : "))
    if n == 0 :
        raise ZeroDivisionError
    x = 23 / n
except ZeroDivisionError:
    print("Zero")