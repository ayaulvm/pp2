#Write a Python program with builtin function that accepts a string and 
# calculate the number of upper case letters and lower case letters
def count_case(s):
    upper_count = sum(1 for char in s if char.isupper())  
    lower_count = sum(1 for char in s if char.islower())  
    
    print(f"Uppercase letters: {upper_count}")
    print(f"Lowercase letters: {lower_count}")


text = input()
count_case(text)


