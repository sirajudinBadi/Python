# def greet_decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f"Arguments : {args}")
#         return func(*args, **kwargs)
#     return wrapper

# @greet_decorator
# def greet(a, b):
#     print(a+b)

# greet(4, 6)

# Admin only decorator
def access_decorator(func):
    def wrapper(user, *args, **kwargs):
        if user.lower() != "admin":
            print("Access Denied.")
        else:
            return func(user, *args, **kwargs)
    return wrapper

@access_decorator
def user_role(role):
    print(f"User is {role}.")

# user_role("adm")

def check_positives(func):
    def wrapper(*args, **kwargs):
        if all(arg > 0 for arg in args if isinstance(arg, (int, float))):
            return func(*args, **kwargs)
        else:
            print("Please provide all the numbers as positive integer or float.")
    return wrapper

@check_positives
def multiply(a,b):
    print(a*b)

multiply(234, 4)