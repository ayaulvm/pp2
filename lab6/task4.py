#Write a Python program that invoke square root function after specific milliseconds.
import math
import time

num = float(input("Enter a number: "))
delay = int(input("Enter delay in milliseconds: "))

time.sleep(delay / 1000)

result = math.sqrt(num)


print(f"Square root of {num} after {delay} milliseconds is {result}")
