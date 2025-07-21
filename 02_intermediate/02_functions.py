def isPrime(num):
    if num<2:
        return False

    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
            
    return True

# n = int(input("Please input the digit : "))

# for i in range(2, n+1):
#     if isPrime(i):
#         print(i, end=", ")
#     else:
#         continue
# print()

count = 0
num = 2
nums = []
while count<50:
    if isPrime(num):
        nums.append(num)
        count+=1
        num+=1
    else:
        num+=1
print(nums)
print(len(nums))