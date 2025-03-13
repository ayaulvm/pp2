#Write a Python program with builtin function to multiply all the numbers in a list
import math
def multiply_list(numbers):
    return math.prod(numbers) 
nums = list(map(int, input().split()))
result = multiply_list(nums)
print(f"Product of {nums} is {result}")
